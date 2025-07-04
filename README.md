# FIR Filter for Audio Noise Reduction in Python

**Digital Signal Processing Project**  
**Title:** *Implementation of Finite Impulse Response Filter (FIR) for Noise Reduction in Audio Signals*  


---

##  Objective

To reduce unwanted noise such as **fan hum** and **white noise** from `.wav` audio recordings using:

- A **Band-pass FIR (Finite Impulse Response) Filter**
- An **Adaptive Wiener Filter**

---

##  Project Structure

```
project-root/
├── resource/       # Contains input and output WAV files
├── main.py         # Implements FIR filter using SciPy
├── we.py           # Applies Wiener filter
└── README.md       # This file
```

---

##  Methodology

### 1.  Audio Data Acquisition

Audio was recorded in a noisy indoor environment and stored in `.wav` format for processing.

```python
from scipy.io import wavfile
fs, audio = wavfile.read("resource/output.wav")
```

---

### 2.  FIR Filter Design

A **band-pass FIR filter** was created using `scipy.signal.firwin` to pass frequencies between 1000 Hz and 5000 Hz:

```python
from scipy.signal import firwin

fir_coeff = firwin(numtaps=301, cutoff=[1000, 5000], pass_zero=False)
```

- **Cutoff Frequencies:** 1000 Hz – 5000 Hz  
- **Filter Length:** 301 taps (longer filter = sharper cutoff)

---

### 3.  FIR Filter Application

The filter was applied using digital convolution (`lfilter`) to suppress low and high-frequency noise:

```python
from scipy.signal import lfilter

filtered_audio = lfilter(fir_coeff, 1.0, audio)
```

---

### 4.  Wiener Filtering

An adaptive Wiener filter was used to further reduce remaining white noise:

```python
from scipy.signal import wiener

filtered_audio = wiener(filtered_audio, mysize=20)
```

- **Window size (`mysize`):** 20 (balance between noise smoothing and signal detail)

---

##  Results and Observations

- **Fan hum (low-frequency noise)** and **white noise (high-frequency hiss)** were significantly reduced.

### FIR Filter:

- Sharp band-pass between 1000–5000 Hz.
- Reduced low-frequency rumble and high-frequency noise outside the speech range.

### Wiener Filter:

- Adaptively smoothed the residual noise.
- Enhanced clarity by reducing hiss while preserving important signal features.

---

##  Conclusion

This project successfully demonstrated the practical use of classical DSP techniques — **FIR filtering** and **Wiener filtering** — for **audio noise reduction** using Python.

> The combined filtering approach significantly improved audio clarity, making it useful for applications like speech enhancement, telecommunication preprocessing, and audio restoration.

---

##  References

- Oppenheim & Schafer — *Discrete-Time Signal Processing*
- R.G. Lyons — *Understanding Digital Signal Processing*
- SciPy Documentation: [`scipy.signal.firwin`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html)
- Stanford EE264 Lecture on [Wiener Filtering](https://web.stanford.edu/class/archive/ee/ee264/ee264.1072/mylecture12.pdf)
- MIT OCW — *Signals, Systems and Inference* (Chapter on Wiener Filtering)

---
