"""
Conductance is calculated by measuring the quantity of gas (the volume of the gas at a known pressure) that passes
a plane in a known time divided by the difference in pressure at two points where the pressure is measured. It is a
purely geometrical quantity that does not depend on pressure, but rather the type of gas, and the geometry.

"""
# TODO: make a database of all the atomic masses of the periodic table

import numpy as np

def conductance_aperture(v,A,a=1):
    """

    :param v: avg velocity of the gas, calculated using func in other file
    :param A: cross sectional area that the gas passes through
    :param a: transmission probability through the tube, default is the result for the long tube and all particles go through
    :return C: conductance of the system in L/s
    """
    C = a*(v*A)/4
    return C*1000

def conductance_circular_tube(v,d,l):
    """
    Conductance of a circular rounded tube calcuations
    :param v: avg boltzmann velocity of a particle
    :param d: diameter of the pipe
    :param l: length of the pipe
    :return: C_tube is conductance of the tube in L/s (multiply by 1000 for L)
    """
    C_tube = (np.pi)*v*d**3/(12*l)
    return C_tube*1000