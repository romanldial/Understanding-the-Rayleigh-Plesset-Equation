cmake_minimum_required(VERSION 3.5)
PROJECT(RayleighPlessetEvolution
        DESCRIPTION "Visualising the Rayleigh Plesset Equation in C++"
        LANGUIAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_executable(RayleighPlessetEvolution main.cpp)
target_compile_features(RayleighPlessetEvolution PRIVATE cxx_std_20)

