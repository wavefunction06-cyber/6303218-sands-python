from signals import t_sinc, y_sinc, t_rect, y_rect
from mods import modify_sinc, modify_rect
import matplotlib.pyplot as plt

"""VARIABLES BAR"""
t_sinc_mod, y_sinc_mod = modify_sinc(amplitude=2, offset=0.5, phase=5, stretch=4)
t_rect_mod, y_rect_mod = modify_rect(amplitude=6, offset=-2, phase=0.5, width=5)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t_sinc, y_sinc, label='Original', alpha=0.5)
plt.plot(t_sinc_mod, y_sinc_mod, label='Modified')
plt.title('Sinc Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t_rect, y_rect, label='Original', alpha=0.5)
plt.plot(t_rect_mod, y_rect_mod, label='Modified')
plt.title('Rectangular Pulse')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()