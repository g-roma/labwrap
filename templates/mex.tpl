#include "mex.h"
#include "{{header}}"

void mexFunction(int nouts, mxArray *outs[], int nins, const mxArray *ins[])
{
    // validation
    if (nins != {{arguments|length}}) {
        mexErrMsgTxt("there should be {{n_ins}} input arguments");
    } else if (nouts != 1) {
       mexErrMsgTxt("there should be 1 output argument");
    }

    // input arguments
    {% for arg in arguments %}
        {% if arg.meta_type=="2D" %}
            int x = mxGetM( ins[ {{ loop.index0 }} ] );
            int y = mxGetN( ins[ {{ loop.index0 }} ] );
            {{map_type}} {{arg.name}}( mxGetPr(ins[ {{ loop.index0 }} ]), x, y);
        {% elif arg.meta_type=="1D" %}
        TODO
        {% elif arg.meta_type=="scalar" %}
            {{arg.type}} {{arg.name}} = ({{arg.type}}) mxGetScalar(ins[ {{ loop.index0 }} ]);
        {% endif %}
    {% endfor %}

    // actual function call
    {{return_value.type}} result = {{function_name}}(
        {% for arg in arguments %}
            {{arg.name}}{% if not loop.last %},{% endif%}
        {% endfor %}
    );

    // return value
    {% if return_value.meta_type == "2D" %}
        {{map_type}}( mxGetPr(outs[0]), result.{{return_value.rows}}, result.{{return_value.cols}} ) = result;
    {% elif return_value.meta_type=="1D" %}
        TODO
    {% elif return_value.meta_type == "scalar" %}
         mxGetPr(outs[0]) = ({{arg.type}}) result;
    {% endif %}
    return;
 }