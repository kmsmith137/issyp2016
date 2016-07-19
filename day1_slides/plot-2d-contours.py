#!/usr/bin/env python

import numpy as np
import numpy.random as rand

import matplotlib.pyplot as plt


def make_x(shape):
    r = rand.uniform(low=1., high=2., size=shape)
    theta = rand.uniform(low=0., high=np.pi/2., size=shape)
    return (r * np.cos(theta) - 3./np.pi, r * np.sin(theta) - 3./np.pi)


def make_z(n,m):
    (x, y) = make_x(shape=(n,m))
    x = np.sum(x, axis=1) / m**0.5
    y = np.sum(y, axis=1) / m**0.5
    return (x, y)


(x,y) = make_x(1000000)
plt.hexbin(x, y, gridsize=100, extent=[-2,2,-2,2])
plt.savefig('xhex.png')
plt.clf()

(x,y) = make_z(1000000, 2)
plt.hexbin(x, y, gridsize=100, extent=[-2,2,-2,2])
plt.savefig('zhex2.png')
plt.clf()

(x,y) = make_z(1000000, 5)
plt.hexbin(x, y, gridsize=100, extent=[-2,2,-2,2])
plt.savefig('zhex5.png')
plt.clf()

(x,y) = make_z(1000000, 20)
plt.hexbin(x, y, gridsize=100, extent=[-2,2,-2,2])
plt.savefig('zhex20.png')
plt.clf()

(x,y) = make_z(1000000, 100)
plt.hexbin(x, y, gridsize=100, extent=[-2,2,-2,2])
plt.savefig('zhex100.png')
plt.clf()
