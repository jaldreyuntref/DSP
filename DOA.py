import numpy as np

def doa(delays, distance):
    angles = 0
    for delay in delays:
        angles += np.degrees(np.arccos((delay * 343) / (distance )))
        
    return angles / len(delays)
