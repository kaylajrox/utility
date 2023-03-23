import numpy as np

def find_nearest_idx(array, value):
    """
    Similar to where or argwhere in numpy. Given a value, find the index of an element in an array closest to given value.
    --------
    params: array: array to inspect
            value: value we are using for comparison
    return: idx: index of the element which closely matches the value
    """
    idx = (np.abs(array - value)).argmin()
    return idx