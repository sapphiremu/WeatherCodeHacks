# altitude correction
# ©Saffron Murcia 2023
# v 0.1
# Code to provide the pressure variance in MB at altitude in 
# metres that will need to be added to raw pressure readings 
# for standard readouts.
from math import exp
def airPressureDecrement(alt, tempC = 20):
    REF_PRESSURE = 101325 # Reference pressure at sea level
    REF_ALTITUDE = 0
    # There is no reason to change G, M or R unless this software
    # is to be used on another planet.
    G = 9.80665 # Metres per second squared
    M = 0.0289644 # Molar mass of air
    R = 8.31432 # Universal gas constant
    tempK = 273 + tempC # tempC in kelvins
    pressure = REF_PRESSURE * exp(-G * M * (alt - REF_ALTITUDE)/(R * tempK))
    pressureReduction = (REF_PRESSURE - pressure)/100
    return (pressureReduction)
