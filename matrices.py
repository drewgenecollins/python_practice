#!/usr/bin/python3

from random import *
import numpy as nm

a =[[5, 3],
   [4, 8]]
b= a[0][1]
print(b)



r=[0]
for i in range(50):
    a=random()
    r.insert(i, a)

#print (raw)
b = nm.mean(r)
c = nm.std(r)
print('%.3f'%b)
print('%.3f'%c)
print('mean and standard deviation')
