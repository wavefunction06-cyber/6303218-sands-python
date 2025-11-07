from my_signals import mysinc, myrect, mysaw, mystep
from mods import (
    modify_sinc,
    modify_rect,
    modify_saw,
    modify_step,
    compute_fft
)
import numpy as np
import matplotlib.pyplot as plt

"""VARIABLES BAR"""
SR = 1000
T0 = -3.0
T1 =  3.0
F_SAW = 0.5

WHICH_FFT = "saw"   # "sinc" | "rect" | "saw" | "step" | None
FFT_DB = False
FFT_ONLY_POS = True
FFT_NORMALIZE = True

# Base generated signals (sinc, rect, saw, step)
t_sinc, y_sinc = mysinc(duration=50, sample_rate=SR)
t_rect, y_rect = myrect(pulse_width=1.0, duration=4.0, sample_rate=SR)
t_saw,  y_saw  = mysaw(frequency=F_SAW, start_time=T0, end_time=T1, amplitude=1.0, sample_rate=SR, symmetry=0.0)
t_step, y_step = mystep(step_time=0.0, start_time=T0, end_time=T1, sample_rate=SR, high=1.0)

# Modified signals
t_sinc_mod, y_sinc_mod = modify_sinc(amplitude=2, offset=0.5, phase=5, stretch=4)
t_rect_mod, y_rect_mod = modify_rect(amplitude=6, offset=-2, phase=0.5, width=5)
t_saw_mod,  y_saw_mod  = modify_saw(amplitude=1.5, offset=0.2, phase=0.3, stretch=1.2)
t_step_mod, y_step_mod = modify_step(amplitude=1.0, offset=-0.3, phase=0.1, stretch=1.0)

def pick_signal(which):
    if which == "sinc":
        return t_sinc, y_sinc, "Sinc"
    if which == "rect":
        return t_rect, y_rect, "Rect"
    if which == "saw":
        return t_saw, y_saw, "Sawtooth"
    if which == "step":
        return t_step, y_step, "Unit Step"
    return None, None, ""

# 2×2 comparison (original vs modified)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t_sinc, y_sinc, label='Original', alpha=0.5)
plt.plot(t_sinc_mod, y_sinc_mod, label='Modified')
plt.title('Sinc'); plt.xlabel('Time [s]'); plt.ylabel('Amplitude'); plt.grid(); plt.legend()

plt.subplot(2, 2, 2)
plt.plot(t_rect, y_rect, label='Original', alpha=0.5)
plt.plot(t_rect_mod, y_rect_mod, label='Modified')
plt.title('Rect'); plt.xlabel('Time [s]'); plt.ylabel('Amplitude'); plt.grid(); plt.legend()

plt.subplot(2, 2, 3)
plt.plot(t_saw, y_saw, label='Sawtooth', alpha=0.8)
plt.plot(t_saw_mod, y_saw_mod, label='Modified', alpha=0.8)
plt.title('Sawtooth'); plt.xlabel('Time [s]'); plt.ylabel('Amplitude'); plt.grid(); plt.legend()

plt.subplot(2, 2, 4)
plt.plot(t_step, y_step, label='Unit Step', drawstyle='steps-post', alpha=0.8)
plt.plot(t_step_mod, y_step_mod, label='Modified', drawstyle='steps-post', alpha=0.8)
plt.title('Unit Step'); plt.xlabel('Time [s]'); plt.ylabel('Amplitude'); plt.grid(); plt.legend()

plt.tight_layout()
plt.show()

# Optional FFT for any selected function (using compute_fft from mods.py)
if WHICH_FFT in {"sinc", "rect", "saw", "step"}:
    if WHICH_FFT == "sinc":
        t_sel, y_sel, name = t_sinc, y_sinc, "Sinc"
    elif WHICH_FFT == "rect":
        t_sel, y_sel, name = t_rect, y_rect, "Rect"
    elif WHICH_FFT == "saw":
        t_sel, y_sel, name = t_saw, y_saw, "Sawtooth"
    else:
        t_sel, y_sel, name = t_step, y_step, "Unit Step"

    if len(t_sel) > 1:
        f, Y = compute_fft(t_sel, y_sel, only_positive=FFT_ONLY_POS, normalize=FFT_NORMALIZE)
        mag = np.abs(Y)
        if FFT_DB:
            mag = 20 * np.log10(np.maximum(mag, 1e-12))

        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(t_sel, y_sel, label=f'{name} (time)')
        plt.title(f'{name} (Time)')
        plt.xlabel('Time [s]'); plt.ylabel('Amplitude')
        plt.grid(); plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(f, mag, label='|FFT| dB' if FFT_DB else '|FFT|')
        plt.title(f'{name} Spectrum')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Magnitude (dB)' if FFT_DB else 'Magnitude')
        plt.grid(); plt.legend()

        plt.tight_layout()
        plt.show()
