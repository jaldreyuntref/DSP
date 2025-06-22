import numpy as np

def doa(delays, distanceBetweenMics):
    angles = []
    for i, delay in enumerate(delays):
        argument = (delay * 343) / distanceBetweenMics[i]
        if -1 <= argument <= 1:
            angles.append(np.degrees(np.arccos(argument)))
        else:
            print(f"Ignorado: delay={delay:.6f}, distancia={distanceBetweenMics[i]:.3f}, argumento={argument:.3f}")

    if len(angles) == 0:
        return np.nan
    
    return np.mean(angles)
