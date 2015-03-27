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
            int {{arg.name}}_n = mxGetM( ins[ {{ loop.index0 }} ] );
            int {{arg.name}}_m = mxGetN( ins[ {{ loop.index0 }} ] );
            {{map_type}} {{arg.name}}( mxGetPr(ins[ {{ loop.index0 }} ]), {{arg.name}}_n, {{arg.name}}_m);
        {% elif arg.meta_type=="1D" %}
        TODO
        {% elif arg.meta_type=="scalar" %}
            {{arg.type}} {{arg.name}} = ({{arg.type}}) mxGetScalar(ins[ {{ loop.index0 }} ]);
        {% endif %}
    {% endfor %}

    // actual function call
    {{return_value.type}} result = {{function_name}}(
        {% for arg in arguments %}{{arg.name}}{% if not loop.last %},{% endif%}{% endfor %}
    );

    // return value
    {% if return_value.meta_type == "2D" %}
        outs[0] = mxCreateDoubleMatrix(result.{{return_value.rows}} ,result.{{return_value.cols}}, mxREAL);
        {{map_type}}( mxGetPr(outs[0]), result.{{return_value.rows}}, result.{{return_value.cols}} ) = result;
    {% elif return_value.meta_type=="1D" %}
        TODO
    {% elif return_value.meta_type == "scalar" %}
         {{return_value.type}} *out = mxGetPr(outs[0]);
         *out=result;
    {% endif %}
    return;
 }