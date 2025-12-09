// Imports PhysicalConstants.json   (SI Units)

#pragma once
#include <string>
#include <fstream>
#include "json.hpp"

struct PhysicalConstants {
    double rhoL;      // kg/m^3   (liquid density)
    double nuL;       // m^2/s    (kinematic viscosity)
    double S;         // N/m      (surface tension)
    double R0;        // m        (inital radius)
    double k;         //          (polytropic exponent)
    double p_v;       // Pa       (vapor pressure of liquid)
    double pG0;       // Pa       (gas pressure at R0)
};

PhysicalConstants loadConstants(const std::string& filename);