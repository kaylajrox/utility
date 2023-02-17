import scipy.constants as cts
import numpy as np

pi = np.pi

kB = cts.value('Boltzmann constant') # Boltzmann constant in J/K
N = cts.value('Avogadro constant') # in particles/mol

def convert_atomic_mass_kg(molecular_weight):
    """
    Converts an atomic mass to a mass in kg by converting the atomic weight into SI kg. Molecular weight divided by N
    gets everything in grams, and dividing by 1000 gives it in kg
    :param molecular_weight: periodic table molecular weight
    :return m_kg: mass in kg
    """
    m_kg = (molecular_weight/N)/1000
    return m_kg

def convert_celsius_to_kelvin(T_C):
    """
    Convert celsius to kelvin with T in celsius
    :param T_C: temperature in celsius
    :return T_K: temperature in Kelvin
    """
    T_K = T_C + 273.15
    return T_K
def avg_boltzmann_velocity(m_atomic,T_C=22):
    """

    :param m_atomic: atomic mass of the given substance
    :param T_C: temperature in celsius, default set to room temperature at 22C
    :return:
    """
    T = convert_celsius_to_kelvin(T_C)
    m_kg = convert_atomic_mass_kg(m_atomic)
    v_avg = np.sqrt(8*kB*T/(pi*m_kg))
    return v_avg


def rms_boltzmann_velocity(m_atomic,T_C=22):
    """

    :param m_atomic: atomic mass of the given substance
    :param T_C: temperature in celsius, default set to room temperature at 22C
    :return:
    """
    T = convert_celsius_to_kelvin(T_C)
    m_kg = convert_atomic_mass_kg(m_atomic)
    v_rms = np.sqrt(3*kB*T/(pi*m_kg))
    return v_rms

