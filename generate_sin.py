#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 15/9/15 17:05

"""
import math

interval = math.pi / 32
value_sin = []

for i in range(0, 32):
    value_sin.append(math.sin(interval * i) * 200)

print(value_sin, len(value_sin))
