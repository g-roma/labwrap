#!/usr/bin/env python

import sys, argparse, re, jinja2

MEX_TEMPLATE = "templates/mex.tpl"

def parse_header(in_file):
  
  parsed_funcs =[]

  for line in open(in_file):
    if(line[0]=="#" or line.isspace()):continue
    return_type = re.compile("^\s*(\S+)\s*").search(line).group(1)
    func_name = re.compile("\s*(\S+)\s*\(").search(line).group(1)
    argument_list = re.compile("\((.+)\)").search(line).group(1)
    arguments = {}
    for arg in argument_list.split(","):
      argtype,argname = arg.strip().split(" ")
      arguments[argname.strip()]=argtype.strip()
    parsed_funcs.append({"function_name":func_name,"return_type":return_type,"arguments":arguments})

  return parsed_funcs

def create_func_spec(parsed_func, type_maps):
  arguments = []
  for arg_name, arg_type in parsed_func["arguments"].items():
    arg ={"name":arg_name}
    for k,v in type_maps[arg_type].items():arg[k]=v
    arguments.append(arg)

  spec = {
    "function_name":parsed_func["function_name"],
    "arguments":arguments,
    "return_value" : type_maps[parsed_func["return_type"]]
  }
  return spec

def read_type_maps(file_name):
  typemaps={}
  for line in open(file_name):
    typemap={}
    map_items = line[:-1].split(" ")
    typemap["type"]=map_items[0]
    typemap["meta_type"] = map_items[1]
    if typemap["meta_type"]=="1D": 
      typemap["size"]=map_items[2]
    if typemap["meta_type"]=="2D": 
      typemap["rows"]=map_items[2]
      typemap["cols"]=map_items[3]
    typemaps[map_items[0]]=typemap
  return typemaps

def render_template(func_spec,template_file):
  templateLoader = jinja2.FileSystemLoader( searchpath="./" )
  templateEnv = jinja2.Environment( loader=templateLoader )
  template = templateEnv.get_template(template_file)
  outputText = template.render( func_spec )
  return outputText

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Generate mex wrapper from C header file")
  parser.add_argument("input", nargs=1, help="input header file")
  parser.add_argument("out_dir",nargs=1, help="output directory")
  parser.add_argument("typemaps",nargs=1, help="type maps .csv file")

  args = parser.parse_args()  
  typemaps = read_type_maps(args.typemaps[0])
  parsed_funcs = parse_header(args.input[0])
  
  for f in parsed_funcs:
      spec = create_func_spec(f,typemaps)
      spec["header"]="../"+args.input[0]
      spec["map_type"]="Eigen::Map<Eigen::MatrixXd>"#TODO!
      text = render_template(spec,MEX_TEMPLATE)
      fname = args.out_dir[0]+"/"+f["function_name"]+"Mex.cpp"
      outf=open(fname,"wt")
      outf.write(text)
      outf.close()