import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter, freqz

fs, audio = wavfile.read("resource/output.wav") 

if audio.ndim == 2:
    audio = audio.mean(axis=1)

# FIR filter 
numtaps = 301                  
low_cutoff = 1000               
high_cutoff = 5000            
nyquist = fs / 2                

# FIR filter ko band  
band = [low_cutoff / nyquist, high_cutoff / nyquist]

#  Creating FIR filter
fir_coeff = firwin(numtaps, band, pass_zero=False)


plt.figure()
plt.plot(fir_coeff)
plt.title("FIR Filter Coefficients")
plt.xlabel("Tap Index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

#Applying the filter to the audio signal
filtered_audio = lfilter(fir_coeff, 1.0, audio)

#Saveing teh filtered audio
output_int16 = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * 32767)
wavfile.write("filtered_audio.wav", fs, output_int16)
print("Filtered audio saved as 'filtered_audio.wav'")

time = np.arange(len(audio)) / fs
plt.figure(figsize=(12, 4))
plt.plot(time, audio)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Original Audio Waveform')
plt.grid()
plt.show()

w, h = freqz(fir_coeff, worN=8000)
plt.figure()
plt.plot(w * nyquist / np.pi, 20 * np.log10(np.abs(h)))
plt.title("Band-Pass FIR Filter Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.grid()
plt.show()

time = np.arange(len(audio)) / fs
plt.figure(figsize=(12, 4))
plt.plot(time, audio, label='Original')
plt.plot(time, filtered_audio, label='Filtered', alpha=0.7)
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.title('Original vs bandpass Filtered Audio Waveform')
plt.legend()
plt.grid()
plt.show()