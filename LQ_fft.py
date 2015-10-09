#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 7/9/15 18:26

"""

import numpy as np

data = [876, 899, 893, 891, 858, 820, 750, 682, 639, 544, 451, 349, 252, 147, 62, -73, -197, -322, -435, -566, -664,
        -744, -814, -874, -913, -932, -921, -940, -943, -911, -855, -802, -709, -597, -501, -401, -305, -255, -173, -70,
        76, 197, 326, 442, 576, 648, 724, 792, 844, 876, 875, 869, 885, 852, 814, 763, 710, 600, 497, 401, 299, 198, 69,
        -44, -135, -261, -384, -435, -580, -683, -748, -819, -873, -910, -930, -912, -934, -941, -910, -855, -810, -720,
        -604, -502, -403, -304, -200, -71, 24, 138, 267, 392, 484, 581, 687, 758, 793, 847, 882, 896, 894, 892, 860,
        817, 752, 697, 593, 501, 405, 302, 205, 95, -18, -128, -260, -380, -502, -601, -700, -781, -844, -888, -921,
        -933, -936, -939, -942, -917]
data_after_FFT = np.fft.fft(data, 128, )
# print(data_after_FFT)

import numpy as np


def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:
        # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N / 2] * X_odd,
                               X_even + factor[N / 2:] * X_odd])


# print(FFT(data))
print(DFT_slow(data), np.fft.fft(data))

print(np.allclose(DFT_slow(data), np.fft.fft(data)))

# x = np.random.random(1024)

# if __name__ == '__main__':
#     import timeit
#
#     print(timeit.timeit(stmt='np.fft.fft(x)', setup='from __main__ import FFT,np, x'))
#
#     print(timeit.timeit(stmt='FFT(x)', setup='from __main__ import FFT, x'))
#
#
#
