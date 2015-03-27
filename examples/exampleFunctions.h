#include "Eigen/Dense"

Eigen::MatrixXd matrixMatrix(Eigen::Map<MatrixXd> m1, Eigen::Map<MatrixXd> m2);

Eigen::MatrixXd matrixVector(Eigen::Map<MatrixXd> m, Eigen::Map<VectorXd> v);
Eigen::MatrixXd matrixDouble(Eigen::Map<MatrixXd> m, double d);


