#include "Eigen/Dense"

Eigen::MatrixXd matrixMatrix(Eigen::Map<Eigen::MatrixXd> m1, Eigen::Map<Eigen::MatrixXd> m2);

Eigen::MatrixXd matrixVector(Eigen::Map<Eigen::MatrixXd> m, Eigen::Map<Eigen::VectorXd> v);
Eigen::MatrixXd matrixDouble(Eigen::Map<Eigen::MatrixXd> m, double d);


