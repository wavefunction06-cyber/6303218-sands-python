import numpy as np
import matplotlib.pyplot as plt

def mysinc(duration=50, sample_rate=1000):
    t = np.linspace(-duration/2, duration/2, int(sample_rate * duration))
    y = np.sinc(t)
    return t, y

def myrect(pulse_width=1, duration=5, sample_rate=1000):
    t = np.linspace(-duration/2, duration/2, int(sample_rate * duration))
    y = np.where(np.abs(t) <= pulse_width/2, 1, 0) 
    return t, y

t_sinc, y_sinc = mysinc(duration=50)          
t_rect, y_rect = myrect(pulse_width=1, duration=4)

  





