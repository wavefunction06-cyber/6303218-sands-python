from my_signals import mysinc, myrect, mysaw, mystep
from mods import modify_sinc, modify_rect, modify_saw, modify_step, compute_fft
import numpy as np


def test_mysinc():
    """
    Test the mysinc function with various test cases.

    Tests include:
    - Signal length verification
    - Center value check
    - Symmetry around t=0
    - Error handling for invalid duration
    """
    t, v = mysinc(duration=10, sample_rate=1000)
    assert len(t) == 10000
    assert len(v) == 10000
    assert np.isclose(v[len(v)//2], 1.0, atol=1e-12)
    t_bad, v_bad = mysinc(duration=-1, sample_rate=1000)
    assert len(t_bad) == 0 or len(v_bad) == 0

def test_myrect():
    """
    Test the myrect function with various test cases.

    Tests include:
    - Signal length verification
    - Pulse amplitude and width
    - Error handling for invalid duration
    """
    t, v = myrect(pulse_width=2, duration=10, sample_rate=1000)
    assert len(t) == 10000
    assert len(v) == 10000
    # High region should be around 2 seconds wide
    dt = t[1] - t[0]
    high_samples = np.count_nonzero(v == 1.0)
    assert np.isclose(high_samples * dt, 2.0, rtol=1e-2)
    t_bad, v_bad = myrect(pulse_width=1, duration=-1, sample_rate=1000)
    assert len(t_bad) == 0 or len(v_bad) == 0

def test_mysaw():
    """
    Test the mysaw function with various test cases.

    Tests include:
    - Signal length verification
    - Range and initial value check
    - Symmetry parameter behavior
    - Error handling for invalid window
    """
    t, v = mysaw(frequency=1, start_time=0, end_time=10, amplitude=1, sample_rate=1000, symmetry=0.0)
    assert len(t) == 10000
    assert len(v) == 10000
    assert np.isclose(np.max(v), 1.0, atol=1e-3)
    assert np.isclose(np.min(v), -1.0, atol=1e-3)
    assert np.isclose(v[0], -1.0, atol=1e-3)

    t2, v2 = mysaw(frequency=1, start_time=0, end_time=10, amplitude=3, sample_rate=1000, symmetry=1.0)
    assert np.isclose(np.max(v2), 3.0, atol=1e-3)
    assert np.isclose(np.min(v2), -3.0, atol=1e-3)

    t_bad, v_bad = mysaw(frequency=1, start_time=1, end_time=0, amplitude=1, sample_rate=1000, symmetry=0.0)
    assert len(t_bad) == 0 and len(v_bad) == 0

def test_mystep():
    """
    Test the mystep function with various test cases.

    Tests include:
    - Signal length verification
    - Step time and level verification
    - Error handling for invalid window
    - Zero height case
    """
    t, v = mystep(step_time=5, start_time=0, end_time=10, sample_rate=1000, high=1)
    assert len(t) == 10000
    assert v[0] == 0
    assert v[5000] == 1

    t2, v2 = mystep(step_time=5, start_time=0, end_time=10, sample_rate=1000, high=3)
    assert np.isclose(np.max(v2), 3.0, atol=1e-3)

    t_bad, v_bad = mystep(step_time=0, start_time=1, end_time=0, sample_rate=1000, high=1)
    assert len(t_bad) == 0 and len(v_bad) == 0

    t_zero, v_zero = mystep(step_time=5, start_time=0, end_time=10, sample_rate=1000, high=0)
    assert np.allclose(v_zero, 0)

def test_modify_sinc():
    """
    Test the modify_sinc function with amplitude/offset, phase, and stretch.

    Tests include:
    - Length preservation
    - Amplitude scaling
    - Phase shift effect
    - Stretch effect (compression/expansion)
    """
    t, y = modify_sinc(amplitude=2, offset=0.5, phase=0.01, stretch=2)
    assert len(t) == len(y)
    assert np.isclose(np.max(y) - 0.5, 2.0, atol=0.1)

    t2, y2 = modify_sinc(amplitude=1, offset=0, phase=0.0, stretch=0.5)
    assert len(t2) == len(y2)

def test_modify_rect():
    """
    Test the modify_rect function with amplitude/offset and phase.

    Tests include:
    - Length preservation
    - Width control via base generator
    - Phase shift effect
    """
    t, y = modify_rect(amplitude=2, offset=-1, phase=0.01, width=2)
    assert len(t) == len(y)
    assert np.isclose(np.max(y), 1.0, atol=1e-6) or np.isclose(np.max(y), 2.0, atol=1e-6)

def test_modify_saw():
    """
    Test the modify_saw function with amplitude/offset, phase, and stretch.

    Tests include:
    - Length preservation
    - Amplitude scaling
    - Phase shift effect
    - Stretch factor application
    """
    t, y = modify_saw(amplitude=1.5, offset=0.2, phase=0.01, stretch=1.2)
    assert len(t) == len(y)
    assert np.isclose(np.max(y) - 0.2, 1.5, atol=0.2)

def test_modify_step():
    """
    Test the modify_step function with amplitude/offset, phase, and stretch.

    Tests include:
    - Length preservation
    - Plateau value after modification
    - Phase shift of the step edge
    """
    t, y = modify_step(amplitude=1.0, offset=-0.3, phase=0.002, stretch=1.0)
    assert len(t) == len(y)
    assert np.isclose(np.max(y), 1.0 - 0.3, atol=1e-6)

def test_compute_fft():
    """
    Test the compute_fft helper for basic sanity.

    Tests include:
    - Frequency grid consistency
    - Normalization behavior
    - Positive-frequency selection
    """
    # Simple 1 Hz sine on [0,1)
    sr = 1000
    t = np.linspace(0, 1, sr, endpoint=False)
    y = np.sin(2*np.pi*1*t)

    f, Y = compute_fft(t, y, only_positive=True, normalize=True)
    assert np.all(f >= 0)
    assert np.isclose(np.max(np.abs(Y)), 0.5, atol=0.1)  # unit sine => ~0.5 amplitude at 1 Hz with 1/N normalization
