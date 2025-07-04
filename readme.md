Digital Signal Processing 

Implementation of Finite Impulse Response Filter (FIR) for Noise Reduction in Audio Signals. 

# FIR Filter for Audio Noise Reduction in Python 🎧

This project implements a **Finite Impulse Response (FIR) band-pass filter** and a **Wiener filter** to reduce noise in audio signals using Python. It's part of the Digital Signal Processing (COMP 407) course at Kathmandu University and was submitted as a mini-project for partial fulfillment of the IV Year/I Semester.

## 📌 Objective

To remove unwanted noise such as **fan hum** and **white noise** from recorded `.wav` audio using:
- Band-pass FIR filter
- Adaptive Wiener filter

## 📂 Project Structure

- `resource/` — Contains input and output WAV files
- `main.py` — Implements FIR filter using SciPy
- `we.py` — Applies Wiener filter
- `README.md` — You are here!

## 📈 Methodology

### 1. Audio Data Acquisition
Audio was recorded in a noisy environment with fan hum and saved in `.wav` format using:
```python
fs, audio = wavfile.read("resource/output.wav")

### 2. FIR Filter Design
A band-pass FIR filter was designed using scipy.signal.firwin:
fir_coeff = firwin(numtaps=301, cutoff=[1000, 5000], pass_zero=False)

### 3. FIR Filter Application
The filter was applied using digital convolution:
filtered_audio = lfilter(fir_coeff, 1.0, audio)

### 4. Wiener Filtering
Residual noise was removed using:
filtered_audio = wiener(filtered_audio, mysize=20)

🎧 Results and Observations

    Fan hum (low freq) and white noise (high freq) were significantly reduced.

    FIR Filter:

        Sharp transition band between 1000–5000 Hz.

        Reduced low-frequency modulation.

    Wiener Filter:

        Adaptive noise suppression using local variance.

        Further reduced residual hiss.

✅ Conclusion

The combined use of band-pass FIR and Wiener filters significantly improved the clarity of noisy audio signals. This project shows how classical DSP techniques can be implemented using high-level tools like Python for real-world applications.