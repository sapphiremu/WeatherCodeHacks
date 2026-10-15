# Wind Direction Averaging
# ©Saffron Murcia 2023
# v 0.1
# Code to provide the average direction of wind over several
# samples. Useful when working with low res windvanes.
# Note of caution: While an average of direction can be taken
# over a time period, it does not always give an improved or
# otherwise totally accurate readout.
# Try it out first, but don't use the results as your primary
# data set.

from math import sin, cos, atan2

SAMPLESIZE = 30
def degreesToRadians(degrees):
    return(degrees*(3.14159/180))
def radiansToDegrees(radians):
    degrees=(radians*(180/3.14159))
    if degrees<0:
        degrees=360+degrees
    return(degrees)

def averageDir(directionDeg):
    if len(direction)>SAMPLESIZE:
        direction.pop(0)
    direction.append(directionDeg)
    for each in direction:
        try:
            ew_vector += sin(degreesToRadians(each))
            ns_vector += cos(degreesToRadians(each))
        except:
            ew_vector = sin(degreesToRadians(each))
            ns_vector = cos(degreesToRadians(each))
    ew_average = ew_vector/len(direction)
    ns_average = ns_vector/len(direction)
    return(int(round(radiansToDegrees(atan2(ew_average,ns_average)),0)))
