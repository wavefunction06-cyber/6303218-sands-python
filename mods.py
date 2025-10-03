import numpy as np
from signals import mysinc, myrect

def modify_sinc(amplitude=1, offset=0, phase=0, stretch=1):
    t, y = mysinc(duration=50)
    # Apply stretch by scaling time in interpolation
    y_mod = np.interp(t, (t - phase) / stretch, y, left=0, right=0)
    y_mod = amplitude * y_mod + offset
    return t, y_mod

def modify_rect(amplitude=1, offset=0, phase=0, width=1):
    t, y = myrect(pulse_width=width, duration=4)
    # Shift the signal by interpolating
    y_mod = np.interp(t, t - phase, y, left=0, right=0)
    y_mod = amplitude * y_mod + offset
    return t, y_mod