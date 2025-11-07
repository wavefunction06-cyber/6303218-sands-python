# Signal Generation and Processing

This repository contains scripts to generate, modify, and visualize core 1D signals in Python for study, assignments, or teaching in signal processing, earth sciences, and engineering.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Structure](#structure)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Testing](#testing)
- [Example](#example)
- [Acknowledgements](#acknowledgements)

---

## Description

This project makes it easy to create fundamental signals—such as sinc, rectangular pulse, sawtooth waves, and step functions—and to modify them through amplitude, time shifting, and stretching operations. Fourier/FFT analysis is supported. All functions use numpy and matplotlib for computations and plotting.

---

## Features

- Generate standard signals:
  - Sinc (`mysinc`)
  - Rectangular pulse (`myrect`)
  - Sawtooth waveform (`mysaw`)
  - Unit step function (`mystep`)
- Modify signals:
  - Amplitude scaling, vertical offset
  - Time/phase shifting, time stretching
  - Functions: `modify_sinc`, `modify_rect`, `modify_saw`, `modify_step`
- Fourier Transform:
  - Use `compute_fft` for quick spectral analysis
- Visualize:
  - 2×2 comparison of base and modified signals using matplotlib
- Includes pytest-based testing to validate all signal types and modification functions

---

## Structure

| File           | Description                           |
| -------------- | ------------------------------------- |
| `my_signals.py`| Core signal generation functions      |
| `mods.py`      | Signal modification & FFT utilities   |
| `run.py`       | Script to run and plot signals        |
| `tests.py`     | Pytest unit tests for all features    |
| `requirements.txt` | Python dependencies if needed      |
| `README.md`    | Project documentation                 |


---

## How to use

To run the main demonstration with plotting:
python run.py

This will display plots comparing original and modified versions of each signal type.

You can change which function is analyzed in the frequency domain by editing the `WHICH_FFT` variable in `run.py` (choose from `"sinc"`, `"rect"`, `"saw"`, or `"step"`).

---

## Testing

Run the tests to ensure all functions work as expected:
pytest -q tests.py
A successful test run produces 9 passed tests.

---

## Example

![Passed test]("Images\Passed_test.png")