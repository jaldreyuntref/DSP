import numpy as np
import matplotlib.pyplot as plt
from visualization import plotCorrelationResult

def timeAveragedcrossCorrelation(signal1, signal2, returnDelay=False, graphs=False):
    windowStart = 0 
    windowLength = min(len(signal1), len(signal2))
    ccResult = np.zeros((2 * windowLength) - 1)
    for lag in range(-windowLength + 1, windowLength):
        if lag >= 0:
            cc = np.dot(
                signal1[windowStart:windowStart + windowLength - lag],
                signal2[windowStart + lag: windowStart + lag + windowLength - lag]
                ) / (windowLength - lag)
        else:
            cc = np.dot(
                signal2[windowStart:windowStart + windowLength - (-lag)],
                signal1[windowStart + (-lag): windowStart + (-lag) + windowLength - (-lag)]
                ) / (windowLength - (-lag))
        ccResult[lag + windowLength - 1] = cc

    if returnDelay:
        lags = np.arange(-len(ccResult)//2, len(ccResult)//2)
        delay = abs(lags[np.argmax(ccResult)])
        if graphs:
            plotCorrelationResult(signal1, signal2, ccResult, lags)
        return ccResult, delay

    return ccResult

if __name__ == "__main__":
    # -------------------------------
    # Prueba con impulso débil + ruido
    # -------------------------------
    N = 2048
    delay_samples = 120

    # Señal 1: impulso + ruido 
    np.random.seed(42)
    signal1 = 0.01 * np.random.randn(N) # Llevar el factor de ruido a 0.05 para observar el problema que describimos en el README.
    signal1[N//2] += 1.0  # impulso 

    # Señal 2: mismo impulso desplazado + otro ruido
    np.random.seed(99)
    signal2 = 0.01 * np.random.randn(N) # Llevar el factor de ruido a 0.05 para observar el problema que describimos en el README.
    signal2[N//2 + delay_samples] += 1.0  # impulso desplazado

    # Calcular y graficar la correlación cruzada
    cc = timeAveragedcrossCorrelation(signal1, signal2)
    lags = np.arange(-len(cc)//2, len(cc)//2)

    # Graficar
    plt.figure(figsize=(12, 5))

    plt.subplot(2, 1, 1)
    plt.plot(signal1, label="Señal 1")
    plt.plot(signal2, label="Señal 2", alpha=0.7)
    plt.title("Impulso débil + ruido")
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(lags, cc)
    plt.title("Correlación cruzada temporal")
    plt.xlabel("Retardo (muestras)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show()