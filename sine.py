import numpy as np
import matplotlib.pyplot as plt

freq=3
duration=10
samplerate=1000

t = np.arange(0, duration, 1/samplerate)
wave = np.sin(2*np.pi*freq*t)

plt.plot(t,wave)
plt.title(f"sine wave: {freq} Hz, {duration} s")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()