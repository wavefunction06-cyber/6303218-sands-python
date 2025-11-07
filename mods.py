import numpy as np
from my_signals import mysinc, myrect, mysaw, mystep

def modify_sinc(amplitude=1, offset=0, phase=0, stretch=1):
    """
    Create a modified sinc signal with amplitude/offset, time shift, and stretch.

    Returns
    -------
    t : ndarray
    y_mod : ndarray
    """
    t, y = mysinc(duration=50)
    y_mod = np.interp(t, (t - phase) / max(stretch, 1e-12), y, left=0, right=0)
    y_mod = amplitude * y_mod + offset
    return t, y_mod

def modify_rect(amplitude=1, offset=0, phase=0, width=1):
    """
    Create a modified rectangular pulse with amplitude/offset, width, and shift.

    Returns
    -------
    t : ndarray
    y_mod : ndarray
    """
    t, y = myrect(pulse_width=width, duration=4)
    y_mod = np.interp(t, t - phase, y, left=0, right=0)
    y_mod = amplitude * y_mod + offset
    return t, y_mod

import numpy as np
from my_signals import mysaw, mystep

def modify_saw(amplitude=1.0, offset=0.0, phase=0.0, stretch=1.0):
    """
    Modify the base sawtooth by vertical scale/offset, horizontal shift, and stretch.

    Parameters
    ----------
    amplitude : float
        Vertical scale.
    offset : float
        Vertical shift.
    phase : float
        Horizontal shift in seconds (right for +).
    stretch : float
        Horizontal stretch factor (>1 stretches, <1 compresses).

    Returns
    -------
    t : ndarray
        Same time grid as base sawtooth.
    y_mod : ndarray
        Modified sawtooth.
    """
    # Use a reasonable default base; adjust to your project’s canonical base if needed
    t, y = mysaw(frequency=0.5, start_time=-3, end_time=3, amplitude=1.0, sample_rate=1000, symmetry=0.0)
    stretch = max(float(stretch), 1e-12)
    y_warp = np.interp(t, (t - phase) / stretch, y, left=0.0, right=0.0)
    return t, amplitude * y_warp + offset

def modify_step(amplitude=1.0, offset=0.0, phase=0.0, stretch=1.0):
    """
    Modify the base step by vertical scale/offset, horizontal shift, and stretch.

    Parameters
    ----------
    amplitude : float
        Vertical scale.
    offset : float
        Vertical shift.
    phase : float
        Horizontal shift in seconds (right for +).
    stretch : float
        Horizontal stretch factor (>1 stretches, <1 compresses).

    Returns
    -------
    t : ndarray
        Same time grid as base step.
    y_mod : ndarray
        Modified step signal.
    """
    t, y = mystep(step_time=0.0, start_time=-3, end_time=3, sample_rate=1000, high=1.0)
    stretch = max(float(stretch), 1e-12)
    y_warp = np.interp(t, (t - phase) / stretch, y, left=0.0, right=0.0)
    return t, amplitude * y_warp + offset
def compute_fft(t, y, only_positive=True, normalize=True):
    """
    Compute the FFT of y(t) on an evenly spaced grid.

    Parameters
    ----------
    t : ndarray
        Time samples (uniform spacing).
    y : ndarray
        Signal samples on t.
    only_positive : bool
        If True, return only non-negative frequencies.
    normalize : bool
        If True, divide FFT by N for amplitude normalization.

    Returns
    -------
    f : ndarray
        Frequency axis in Hz.
    Y : ndarray
        Complex FFT values aligned with f.
    """
    dt = float(t[1] - t[0])
    n = len(y)
    Y = np.fft.fft(y)
    f = np.fft.fftfreq(n, d=dt)
    if normalize:
        Y = Y / n
    if only_positive:
        keep = f >= 0
        f, Y = f[keep], Y[keep]
    return f, Y