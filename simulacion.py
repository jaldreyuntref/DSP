import numpy as np
import pyroomacoustics as pra
import matplotlib.pyplot as plt
from CC import timeAveragedcrossCorrelation
from GCC import generalizedCrossCorrelation
from DOA import doa

# Room dimensions (width*length)
roomDimensions = [5, 5, 3]

# Create a room
room = pra.ShoeBox(roomDimensions, fs=16000, max_order=0)

# Sound source position (x,y,z)
sourcePosition = [5, 5, 1.5]

# Load or generate a simple signal
duration = 1.0  
fs = 16000  
time = np.linspace(0, duration, int(fs * duration))
np.random.seed(42)
impulse = 0.05 * np.random.randn(len(time))
impulse[(len(time))//2] += 1.0  # impulso "escondido"

# Add the source to the room
room.add_source(sourcePosition, signal=impulse)

# Define a linear Microphone Array: 4 mics in a row
distanceBetweenMics = 0.5
initialMicPosition = [1.5, 2.5, 1.5]

# Calculate positions for 4 microphones
micPositions = np.array([
    [initialMicPosition[0] + i * distanceBetweenMics, 
     initialMicPosition[1],
     initialMicPosition[2]]
    for i in range(4)
])

# Add microphones to the room
room.add_microphone_array(pra.MicrophoneArray(micPositions.T, room.fs))

# Run the room simulation
room.simulate()

# Get the microphone signals
micSignals = room.mic_array.signals
numberSamples = micSignals.shape[1]
timeAxis = np.linspace(0, numberSamples / room.fs, numberSamples)

# Plot the signals received by each microphone
plt.figure(figsize=(10, 6))
for i in range(4):
    plt.plot(timeAxis, micSignals[i], label=f'Mic {i+1}')
plt.legend()
plt.title('Signals recibidas por cada micrófono')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()

# Aplicación de CC:
print("-----------------Time Averaged Cross Correlation-----------------")
delays = []
for i in range(3):
    delays.append((timeAveragedcrossCorrelation(micSignals[i], micSignals[i + 1], returnDelay=True, graphs=False)[1]) / fs)

print("Delays between microphones (in seconds):", delays)

print("DOA time averaged cross correlation: ", doa(delays, distanceBetweenMics))

# Aplicación de GCC->CLASSIC:
print("-----------------Classic Cross Correlation-----------------")
delays = []
for i in range(3):
    delays.append((generalizedCrossCorrelation(micSignals[i], micSignals[i + 1], mode='classic', returnDelay=True, graphs=False)[1]) / fs)

print("Delays between microphones (in seconds):", delays)

print("DOA classic cross correlation: ", doa(delays, distanceBetweenMics))

# Aplicación de GCC->SCOT:
print("-----------------SCOT-----------------")
delays = []
for i in range(3):
    delays.append((generalizedCrossCorrelation(micSignals[i], micSignals[i + 1], mode='scot', returnDelay=True, graphs=False)[1]) / fs)

print("Delays between microphones (in seconds):", delays)

print("DOA SCOT: ", doa(delays, distanceBetweenMics))

# Aplicación de GCC->PHASE:
print("-----------------Phase-----------------")
delays = []
for i in range(3):
    delays.append((generalizedCrossCorrelation(micSignals[i], micSignals[i + 1], mode='phase', returnDelay=True, graphs=False)[1]) / fs)

print("Delays between microphones (in seconds):", delays)

print("DOA Phase: ", doa(delays, distanceBetweenMics))