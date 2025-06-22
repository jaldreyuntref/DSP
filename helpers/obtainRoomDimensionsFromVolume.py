import numpy as np

def obtainRoomDimensionsFromVolume(volume):
    z = 3  
    baseArea = volume / z
    side = np.sqrt(baseArea)
    return [side, side, z]