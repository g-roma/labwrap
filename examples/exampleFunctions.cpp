/*
Some example functions using Eigen types.
 */


#include "Eigen/Dense"
#include "exampleFunctions.h"

using namespace Eigen;

MatrixXd matrixMatrix(Map<MatrixXd> m1, Map<MatrixXd> m2){
	return m1*m2;
}

MatrixXd matrixVector(Map<MatrixXd> m, Map<VectorXd> v){
	return m*v;
}

MatrixXd matrixDouble(Map<MatrixXd> m, double d){
	return m*d;
}


int main(void)
{
}

