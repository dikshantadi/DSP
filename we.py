import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import wiener

# === Step 1: Load audio ===
fs, audio = wavfile.read("filtered_audio.wav")

# Normalize if audio is integer type
if np.issubdtype(audio.dtype, np.integer):
    audio = audio / np.max(np.abs(audio))

# === Step 2: Apply Wiener filter ===
# mysize controls the filter window size; bigger -> smoother but more latency
filtered_audio = wiener(audio, mysize=20)

# === Step 3: Save filtered audio ===
output_int16 = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * 32767)
wavfile.write("wiener_filtered_audio.wav", fs, output_int16)
print("Filtered audio saved as 'wiener_filtered_audio.wav'")

# === Step 4: Plot waveforms ===
time = np.arange(len(audio)) / fs
plt.figure(figsize=(12, 4))
plt.plot(time, audio, label='Original')
plt.plot(time, filtered_audio, label='Wiener Filtered', alpha=0.7)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Original vs Wiener Filtered Audio')
plt.legend()
plt.grid()
plt.show()