import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Define the function f(t) = exp(-pi * t^2)
def f(t):
    return np.exp(-np.pi * t**2)

# Parameters
N = 1024
T = 1.0 / 64
t = np.linspace(-N/2*T, N/2*T, N, endpoint=False)
y = f(t)

# FFT with scipy
yf_scipy = fftshift(fft(y)) * T
xf = fftshift(fftfreq(N, T))
FT_exact = np.exp(-np.pi * xf**2)

# FFT with numpy
yf_numpy = np.fft.fftshift(np.fft.fft(y)) * T
xf_numpy = np.fft.fftshift(np.fft.fftfreq(N, T))

# Plot with subplot_mosaic
fig, axs = plt.subplot_mosaic([["scipy", "numpy"]], figsize=(7, 5), layout="constrained", sharey=True)

# Scipy FFT
axs["scipy"].plot(xf, FT_exact, 'k-', linewidth=1.5, label='Exact FT')
axs["scipy"].plot(xf, np.real(yf_scipy), 'r--', linewidth=1, label='FFT (scipy)')
axs["scipy"].set_xlim(-6, 6)
axs["scipy"].set_ylim(-1, 1)
axs["scipy"].set_title("Scipy FFT")
axs["scipy"].set_xlabel("Frequency")
axs["scipy"].set_ylabel("Amplitude")
axs["scipy"].legend()
axs["scipy"].grid(False)

# NumPy FFT
axs["numpy"].plot(xf_numpy, FT_exact, 'k-', linewidth=1.5, label='Exact FT')
axs["numpy"].plot(xf_numpy, np.real(yf_numpy), 'b--', linewidth=1, label='FFT (numpy)')
axs["numpy"].set_xlim(-6, 6)
axs["numpy"].set_title("NumPy FFT")
axs["numpy"].set_xlabel("Frequency")
axs["numpy"].legend()
axs["numpy"].grid(False)

plt.suptitle("Comparison of FFT Implementations vs. Exact Fourier Transform", fontsize=14)
plt.show()