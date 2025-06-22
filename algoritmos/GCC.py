import sys
import os
sys.path.append(os.path.abspath('..'))

import numpy as np
import matplotlib.pyplot as plt
from helpers.visualization import plotCorrelationResult
from scipy.fft import fft, ifft, fftshift
from scipy.signal import get_window

def generalizedCrossCorrelation(signal1, signal2, mode='classic', returnDelay=False, graphs=False):
    crossSpecctrumResult = crossSpectrum(signal1, signal2, mode=mode)
    gccResult = ifft(crossSpecctrumResult)
    gccResult = fftshift(np.real(gccResult))

    if returnDelay:
        lags = np.arange(-len(gccResult)//2, len(gccResult)//2)
        delay = lags[np.argmax(gccResult)]
        if graphs:
            plotCorrelationResult(signal1, signal2, gccResult, lags)

        return gccResult, delay

    return gccResult

def crossSpectrum(signal1, signal2, frameSize=1024, jumpSize=512, windowType='hann', mode='classic'):
    window = get_window(windowType, frameSize)
    numFrames = (len(signal1) - frameSize) // jumpSize + 1
    crossSpec = np.zeros(frameSize, dtype=np.complex64)

    if mode == 'scot':
        power1 = np.zeros(frameSize)
        power2 = np.zeros(frameSize)
    elif mode == 'roth':
        power1 = np.zeros(frameSize)

    for frame in range(numFrames):
        start = frame * jumpSize
        end = start + frameSize

        frame1 = signal1[start:end] * window
        frame2 = signal2[start:end] * window

        Y1 = fft(frame1, n=frameSize)
        Y2 = fft(frame2, n=frameSize)

        if mode == 'scot':
            power1 += np.abs(Y1) ** 2
            power2 += np.abs(Y2) ** 2
        elif mode == 'roth':
            power1 += np.abs(Y1) ** 2

        crossSpec += Y1 * np.conj(Y2)

    crossSpec /= numFrames

    if mode == 'scot':
        power1 /= numFrames
        power2 /= numFrames
        epsilon = 1e-10
        crossSpec /= (np.sqrt(power1 * power2) + epsilon)
    elif mode == 'roth':
        power1 /= numFrames
        epsilon = 1e-10
        crossSpec /= (power1 + epsilon)
    elif mode == 'phase':
        epsilon = 1e-10
        crossSpec /= (np.abs(crossSpec) + epsilon)

    return crossSpec

if __name__ == "__main__":
    # -------------------------------
    # Prueba con impulso débil + ruido
    # -------------------------------
    N = 2048
    delay_samples = 120

    # Señal 1: impulso + ruido
    np.random.seed(42)
    signal1 = 0.05 * np.random.randn(N)
    signal1[N//2] += 1.0  # impulso "escondido"

    # Señal 2: mismo impulso desplazado + otro ruido
    np.random.seed(99)
    signal2 = 0.05 * np.random.randn(N)
    signal2[N//2 + delay_samples] += 1.0  # impulso desplazado

    # Calcular correlación
    corr = generalizedCrossCorrelation(signal1, signal2, mode='scot')
    lags = np.arange(-len(corr)//2, len(corr)//2)

    # Graficar
    plt.figure(figsize=(12, 5))

    plt.subplot(2, 1, 1)
    plt.plot(signal1, label="Señal 1")
    plt.plot(signal2, label="Señal 2", alpha=0.7)
    plt.title("Impulso débil + ruido")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(lags, corr)
    plt.title("Correlación cruzada espectral")
    plt.xlabel("Retardo (muestras)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show()