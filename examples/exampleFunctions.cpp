/*
Some example functions using Eigen types.
 */

#include "Eigen/Dense"
#include "exampleFunctions.h"

using namespace Eigen;

double matrixTrace(Map<MatrixXd> m){
	return m.trace();
}

MatrixXd matrixDouble(Map<MatrixXd> m, double d){
	return m*d;
}

MatrixXd matrixMatrix(Map<MatrixXd> m1, Map<MatrixXd> m2){
	return m1*m2;
}


int main(void)
{
}

