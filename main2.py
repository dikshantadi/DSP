import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter, freqz

# === Step 1: Load audio ===
fs, audio = wavfile.read("filtered_audio.wav")

# Normalize if audio is integer type
if np.issubdtype(audio.dtype, np.integer):
    audio = audio / np.max(np.abs(audio))

# === Step 2: Design Low-Pass FIR Filter ===
numtaps = 301           # Filter length (more taps = sharper cutoff)
cutoff = 3000           # Cutoff frequency in Hz 
nyquist = fs / 2
normalized_cutoff = cutoff / nyquist

fir_coeff = firwin(numtaps, normalized_cutoff)

# Optional: Plot filter frequency response
w, h = freqz(fir_coeff, worN=8000)
plt.figure()
plt.plot(w * nyquist / np.pi, 20 * np.log10(np.abs(h)))
plt.title("Low-Pass FIR Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.grid()
plt.show()

# === Step 3: Apply the filter ===
filtered_audio = lfilter(fir_coeff, 1.0, audio)

# === Step 4: Save filtered audio ===
output_int16 = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * 32767)
wavfile.write("lowpass_filtered_audio.wav", fs, output_int16)
print("Filtered audio saved as 'lowpass_filtered_audio.wav'")

# === Step 5: Plot waveforms ===
time = np.arange(len(audio)) / fs
plt.figure(figsize=(12, 4))
plt.plot(time, audio, label='Original')
plt.plot(time, filtered_audio, label='Filtered', alpha=0.7)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Original vs Low-Pass Filtered Audio Waveform')
plt.legend()
plt.grid()
plt.show()