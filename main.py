import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter, freqz

# === Step 1: Load the audio file ===
fs, audio = wavfile.read("resource/output.wav")  # Change path if needed

# === Step 2: Design FIR Band-Pass Filter ===
numtaps = 101                   # Number of filter taps (higher = sharper)
low_cutoff = 300                # Low cutoff frequency in Hz
high_cutoff = 3400              # High cutoff frequency in Hz
nyquist = fs / 2                # Nyquist frequency

# Normalized cutoff frequencies for bandpass filter
band = [low_cutoff / nyquist, high_cutoff / nyquist]

# Create bandpass FIR filter coefficients
fir_coeff = firwin(numtaps, band, pass_zero=False)

# === Optional: Plot FIR filter coefficients ===
plt.figure()
plt.plot(fir_coeff)
plt.title("FIR Filter Coefficients")
plt.xlabel("Tap Index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# === Step 3: Apply the filter to the audio signal ===
filtered_audio = lfilter(fir_coeff, 1.0, audio)

# === Step 4: Save filtered audio ===
# Rescale filtered audio to int16 for saving
output_int16 = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * 32767)
wavfile.write("filtered_audio.wav", fs, output_int16)
print("Filtered audio saved as 'filtered_audio.wav'")

# === Step 5: Plot full audio waveform ===
time = np.arange(len(audio)) / fs
plt.figure(figsize=(12, 4))
plt.plot(time, audio)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Original Audio Waveform')
plt.grid()
plt.show()

# === Step 6: Plot filter frequency response ===
w, h = freqz(fir_coeff, worN=8000)
plt.figure()
plt.plot(w * nyquist / np.pi, 20 * np.log10(np.abs(h)))
plt.title("Band-Pass FIR Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.grid()
plt.show()

# === Step 7: Plot zoomed waveform before and after filtering ===
samples_to_plot = 400
plt.figure(figsize=(10, 4))
plt.plot(audio[:samples_to_plot], label="Original")
plt.plot(filtered_audio[:samples_to_plot], label="Filtered", alpha=0.75)
plt.legend()
plt.title("Zoomed Waveform: Before and After FIR Filtering")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()