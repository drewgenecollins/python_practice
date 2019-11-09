#!/usr/bin/env python3

import random
import numpy

w=numpy.zeros(18)
for i in range(18):
    w[i]=random.randint(14,24)
print(w)