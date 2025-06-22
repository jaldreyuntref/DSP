import numpy as np

def obtainSourcePositionFromAngle(angleDeg, distance, arrayCenterX, arrayCenterY):
    angleRad = np.radians(angleDeg)

    deltaX = distance * np.cos(angleRad)
    deltaY = distance * np.sin(angleRad)

    sourceX = arrayCenterX + deltaX
    sourceY = arrayCenterY + deltaY

    return sourceX, sourceY