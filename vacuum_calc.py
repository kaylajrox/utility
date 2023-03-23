"""
Author: Kayla Rodriguez
Purpose: Provide functions for calculating conductances of various pipes
"""

import numpy as np

def conductance_short_circular_tube(velocity,A,a=1):
    """ The conductance for a short circular tube is equivalent to the conductance of an aperature when a=1
    :param velocity: avg velocity of the gas, calculated using func in other file
    :param A: cross-sectional area that the gas passes through
    :param a: transmission probability through the tube
    :return C: conductance of the system in L/s"""
    C = a*(velocity*A)/4
    return C*1000

def conductance_long_circular_tube(velocity,diameter,l):
    """
    Conductance of a long circular rounded tube calcuations
    :param velocity: avg boltzmann velocity of a particle
    :param diameter: diameter of the pipe
    :param l: length of the pipe
    :return: C_tube is conductance of the tube in L/s (multiply by 1000 for L)
    """
    C_tube = (np.pi)*velocity*diameter**3/(12*l)
    return C_tube*1000