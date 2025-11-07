import numpy as np

def mysinc(duration=50, sample_rate=1000):
    """
    Generate a continuous-time sinc signal over a symmetric time window.

    Parameters
    ----------
    duration : float
        Total time span of the signal in seconds (centered at 0).
    sample_rate : int
        Samples per second used to discretize the signal.

    Returns
    -------
    t : ndarray
        Time axis sampled uniformly from -duration/2 to duration/2.
    y : ndarray
        Samples of sinc(t) where sinc(x) = sin(pi*x)/(pi*x) with sinc(0)=1.
    """
    n = int(sample_rate * duration)
    t = np.linspace(-duration / 2, duration / 2, n, endpoint=True)
    y = np.sinc(t)
    return t, y


def myrect(pulse_width=1.0, duration=5.0, sample_rate=1000):
    """
    Generate a rectangular pulse centered at t = 0.

    Parameters
    ----------
    pulse_width : float
        Total width of the high portion of the pulse.
    duration : float
        Total time span of the signal in seconds (centered at 0).
    sample_rate : int
        Samples per second used to discretize the signal.

    Returns
    -------
    t : ndarray
        Time axis sampled uniformly from -duration/2 to duration/2.
    y : ndarray
        Rectangular pulse equal to 1 for |t| <= pulse_width/2 and 0 otherwise.
    """
    n = int(sample_rate * duration)
    t = np.linspace(-duration / 2, duration / 2, n, endpoint=True)
    y = (np.abs(t) <= (pulse_width / 2)).astype(float)
    return t, y


def mysaw(frequency=0.5, start_time=-3.0, end_time=3.0, amplitude=1.0, sample_rate=1000, symmetry=0.0):
    """
    Generate a sawtooth wave without SciPy.

    Parameters
    ----------
    frequency : float
        Frequency in Hz.
    start_time : float
        Start time in seconds.
    end_time : float
        End time in seconds.
    amplitude : float
        Peak amplitude (range [-amplitude, amplitude]).
    sample_rate : int
        Samples per second.
    symmetry : float
        Fraction in [0,1]; 0.0 yields a rising ramp, 1.0 yields a falling ramp,
        intermediate values produce a piecewise linear shape with breakpoint at
        symmetry * period.

    Returns
    -------
    t : ndarray
        Time array from start_time to end_time (endpoint excluded for uniform spacing).
    y : ndarray
        Sawtooth samples in range [-amplitude, amplitude].
    """
    duration = float(end_time - start_time)
    if duration <= 0:
        return np.array([]), np.array([])
    n = int(sample_rate * duration)
    t = np.linspace(start_time, end_time, n, endpoint=False)

    # Phase in [0,1)
    phase = (t * frequency) % 1.0
    s = float(np.clip(symmetry, 0.0, 1.0))

    if s == 0.0:
        # Rising ramp from -1 to 1
        y = 2.0 * phase - 1.0
    elif s == 1.0:
        # Falling ramp from 1 to -1
        y = 1.0 - 2.0 * phase
    else:
        # Piecewise linear with breakpoint at symmetry
        y = np.empty_like(phase)
        up = phase < s
        y[up] = -1.0 + 2.0 * (phase[up] / s)                 # map [0, s) to [-1, 1)
        y[~up] = 1.0 - 2.0 * ((phase[~up] - s) / (1.0 - s))  # map [s, 1) to [1, -1)

    return t, amplitude * y


def mystep(step_time=0.0, start_time=-3.0, end_time=3.0, sample_rate=1000, high=1.0):
    """
    Generate a unit step function u(t - step_time).

    Parameters
    ----------
    step_time : float
        Step time where the function transitions from 0 to high.
    start_time : float
        Start time in seconds.
    end_time : float
        End time in seconds.
    sample_rate : int
        Samples per second.
    high : float
        Step height (output value for t >= step_time).

    Returns
    -------
    t : ndarray
        Time array from start_time to end_time (endpoint excluded for uniform spacing).
    y : ndarray
        Unit step: 0 for t < step_time and high for t >= step_time.
    """
    duration = float(end_time - start_time)
    if duration <= 0:
        return np.array([]), np.array([])
    n = int(sample_rate * duration)
    t = np.linspace(start_time, end_time, n, endpoint=False)
    y = (t >= step_time).astype(float) * high
    return t, y
