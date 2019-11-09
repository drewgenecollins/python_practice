#!/usr/bin/python3

# goal: use numpy to find mean and STDEV
import numpy
a = ([1, 2, 3, 4, 5])
b = numpy.mean(a)
c = numpy.std(a)
print('%.2f'%b)
print('%.2f'%c)
print('mean = %.2f   ' 'standard deviation = %.2f' %(b,c))


d=range(1,4)
print(d)