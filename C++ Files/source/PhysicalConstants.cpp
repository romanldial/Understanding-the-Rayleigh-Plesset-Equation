#include "PhysicalConstants.hpp"

PhysicalConstants loadConstants(const std::string& filename){
    std::ifstream file(filename);
    nlohmann::json j;
    file >> j;

PhysicalConstants constants;
constants.rhoL    = j["rhoL"];
constants.nuL     = j["nuL"];
constants.S       = j["S"];
constants.R0      = j["R0"];
constants.k       = j["k"];
constants.p_v     = j["p_v"];
constants.pG0     = j["pG0"];

return constants;
}
