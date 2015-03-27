#!/usr/bin/env python

import sys, argparse, re

def parse_header(in_file):
  
  func_specs =[]

  for line in open(in_file):
    if(line[0]=="#" or line.isspace()):continue

    return_type = re.compile("^\s*(\S+)\s*").search(line).group(1)

    func_name = re.compile("\s*(\S+)\s*\(").search(line).group(1)

    argument_list = re.compile("\((.+)\)").search(line).group(1)
    arguments = {}
    for arg in argument_list.split(","):
      argtype,argname = arg.strip().split(" ")
      arguments[argname.strip()]=argtype.strip()

    func_specs.append((return_type,func_name,arguments))

  return func_specs


 
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Generate mex wrapper from C header file")
  parser.add_argument("input", nargs=1, help="input header file")
  parser.add_argument("ouptut",nargs=1, help="output .mex file")
  args = parser.parse_args()  
  print parse_header(args.input[0])
  
  
  #main(args)