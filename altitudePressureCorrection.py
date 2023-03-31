# altitude correction
# ©Saffron Murcia 2023
# v 0.1
# Code to provide the pressure variance at altitude in metres that
# will need to be added to raw pressure readings for standard
# readouts.
from math import exp
def airPressureDecrement(alt, tempC = 20):
    REF_PRESSURE = 101325 # Reference pressure at sea level
    REF_ALTITUDE = 0
    G = 9.80665 # Metres per second squared
    M = 0.0289644 # Molar mass of air
    R = 8.31432 # Universal gas constant
    T = 273 + tempC # 20 C in kelvins
    pressure = REF_PRESSURE * exp(-G * M * (alt - REF_ALTITUDE)/(R * T))
    pressureReduction = (REF_PRESSURE - pressure)/100
    return (pressureReduction)
