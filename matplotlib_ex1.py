#!/usr/bin/env python3

#^comment if using non unix

import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 6 * np.pi, 1000)
y = np.sin(x)
plt.plot(x, np.sin(x))
plt.show()

def update(hello):
    pass
