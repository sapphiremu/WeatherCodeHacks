# altitude correction
# ©Saffron Murcia 2023
# v 0.1
# v 0.2 - Added funcionality for different plantary bodies.
#         Thanks @DeltaDroid for suggestion.
# Code to provide the pressure variance in hPa at altitude in 
# metres that will need to be added to raw pressure readings 
# for standard readouts.
# v 0.2.1 - Moved gas constant to a... constant.

UNIVERSAL_GAS_CONSTANT = 8.31432
from math import exp
def airPressureDecrement(altitude, tempC = 20):
    solarBody = "EARTH"
    planet = { 
        "EARTH" : [101325, 9.80665, 0.0289644],
        "MARS": [6518, 3.721, 0.044]
        }
    
    altitudeReference = 0 # Altitude for the pressureReference
    pressureReference, gravity, molarAirMass = planet[solarBody]
    tempK = 273 + tempC # 20 C in kelvins
    pressure = pressureReference * exp(-gravity * molarAirMass * (altitude - altitudeReference)/(UNIVERSAL_GAS_CONSTANT * tempK))
    pressureReduction = (pressureReference - pressure)/100
    return (pressureReduction)
