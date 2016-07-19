#!/usr/bin/env python

import numpy as np
import numpy.random as rand

import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt


def make_x(shape):
    x = rand.uniform(low=0., high=2*np.pi, size=shape)
    return np.cos(x)

def make_y(n,m):
    x = make_x((n,m))
    return np.sum(x,axis=1)/m

def make_z(n,m):
    x = make_x((n,m))
    return np.sum(x,axis=1)/m**0.5
    

plt.hist(make_x(1000000), bins=50, range=(-2,2))
plt.savefig('xhist.png')
plt.clf()

plt.hist(make_y(1000000,2), bins=50, range=(-2,2))
plt.savefig('yhist2.png')
plt.clf()

plt.hist(make_y(1000000,5), bins=50, range=(-2,2))
plt.savefig('yhist5.png')
plt.clf()

plt.hist(make_y(1000000,20), bins=50, range=(-2,2))
plt.xlim(-2,2)
plt.savefig('yhist20.png')
plt.clf()

plt.hist(make_y(1000000,100), bins=50, range=(-2,2))
plt.xlim(-2,2)
plt.savefig('yhist100.png')
plt.clf()


####################################################################################################


plt.hist(make_z(1000000,2), bins=50, range=(-2,2))
plt.xlim(-2,2)
plt.ylim(0,70000)
plt.savefig('zhist2.png')
plt.clf()

plt.hist(make_z(1000000,5), bins=50, range=(-2,2))
plt.xlim(-2,2)
plt.ylim(0,70000)
plt.savefig('zhist5.png')
plt.clf()

plt.hist(make_z(1000000,20), bins=50, range=(-2,2))
plt.xlim(-2,2)
plt.ylim(0,70000)
plt.savefig('zhist20.png')
plt.clf()

zfinal = make_z(1000000,100)
plt.hist(zfinal, bins=50, range=(-2,2))
plt.xlim(-2,2)
plt.ylim(0,70000)
plt.savefig('zhist100.png')
plt.clf()

xvec = np.linspace(-2,2,200)
pvec = np.exp(-xvec**2) / np.pi**0.5 * 1000000. * (4./50.)
plt.hist(zfinal, bins=50, range=(-2,2))
plt.plot(xvec, pvec, 'r--', lw=3, label=r'$\exp(-x^2)$')
plt.legend(loc='upper right').draw_frame(False)
plt.xlim(-2,2)
plt.ylim(0,70000)
plt.savefig('zhist100_with_curve.png')
plt.clf()
