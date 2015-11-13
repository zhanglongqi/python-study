#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 9/Nov/15 23:21

"""
import numpy as np

a = np.matrix([
    [1, 2, 7, 8],
    [3, 4, 7, 3]
])

b = np.matrix([
    [1, 8],
    [1, 1],
    [0, 2],
    [0, 34],
])

c = a * b
d = np.dot(a, b)

print(c, '\n\n', d)
