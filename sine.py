import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency=1, duration=5, sample_rate=1000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * frequency * t)
    
    plt.plot(t, y)
    plt.title(f'Sine Wave: {frequency} Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()
generate_sine_wave()
