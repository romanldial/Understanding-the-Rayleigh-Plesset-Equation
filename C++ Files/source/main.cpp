#include <iostream>
#include "PhysicalConstants.hpp"

int main() {
    // load constants 
    PhysicalConstants constants = loadConstants("../source/PhysicalConstants.json");

    // print a couple for confirmation
    std::cout << "rhoL = " << constants.rhoL << std::endl;
    std::cout << "R0 = " << constants.R0 << std::endl;
    std::cout << "pG0 = " << constants.pG0 << std::endl;

    return 0;
}
