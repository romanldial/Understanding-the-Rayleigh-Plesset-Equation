cmake_minimum_required(VERSION 3.5)
PROJECT(RPEcpp
        DESCRIPTION "Visualising the Rayleigh Plesset Equation in C++"
        LANGUIAGES CXX)
add_executable(RPEcpp main.cpp)
target_compile_features(RPEcpp PRIVATE cxx_std_20)

