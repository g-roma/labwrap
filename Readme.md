# labwrap.py


labwrap.py is a script for automatically generating wrappers for C/C++ code so that it can be called in common numerical packages such as Matlab or Python/Numpy. At the moment it generates only Matlab mex files. The code is a rough proof of concept coded at the [CW15 Hack Day](http://www.software.ac.uk/cw15/). More target platforms will come.

The general idea is to simplify the problem by focusing on the data types commonly used in such environments, and map them those of C++ libraries that provide similar functionality. At the moment only [Eigen](http://eigen.tuxfamily.org/) is supported.

## how it works
The generation process starts by parsing the function prototypes from a header file. For the moment only plain C functions (with C++ types) are supported. It is unlikely that full object orientation will be ever added, so you are expected to provide a C interface. In addition, a mapping file for all used types needs to be provided. The initial example includes some Eigen classes. From the function specification and the mapping, a [jinja](http://jinja.pocoo.org/) template for the target platform (e.g a template of the MEX file) is populated.

## how to use it
Provided that you have a .h file with your function definitions and a python distribution with the jinja package, the following should work:

```
./labwrap.py path_to_header.h out_dir path_to_mapping.csv

```

To run the example:

```
./labwrap.py examples/exampleFunctions.h mex examples/types_eigen.csv
```

The script assumes that your output directory is at the same level than the directory where the code lives, so that the mex files will ../include your header path.

After generating the mex files, you can compile them on the command line or in matlab:

```
mex  CXXFLAGS="-fPIC -std=c++0x -O3" matrixDouble.cpp ../examples/exampleFunctions.cpp
```

And call them in Matlab...

```

\>> out= matrixDoubleMex(ones(1,2),3)
out =

     3     3     3     3     3     3
