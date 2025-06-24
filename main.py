import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 500  # sampling frequency
t = np.arange(0, 1, 1/fs)  # 1 second
clean_signal = np.sin(2 * np.pi * 50 * t)  # 50 Hz sine wave
noise = np.random.normal(0, 0.5, len(t))  # white Gaussian noise
noisy_signal = clean_signal + noise

plt.plot(t, noisy_signal)
plt.title("Noisy Signal")
plt.show()