# -*- coding: utf-8 -*-

import car
import numpy as np
import pylab as plt
from scipy.signal import place_poles


def car_dyn(x, u):
    """
    Computes the derivative of the car's state vector x according to
    x and the control u
    """

    x, y, teta, v, delta = x
    v1, v2 = u
    xdot = np.array([
           v * np.cos(delta) * np.cos(teta),
           v * np.cos(delta) * np.sin(teta),
           (v * np.sin(delta)) / L_car,
           v1,
           v2
           ])
    return xdot


def observation_func(x, track):
    d = car.dist_to_track(x, track)
    return np.array([d, x[3], x[4]])


L_car = 3  # car length (don't mess it up with L from KLH control)
r0 = 5  # reference distance to track
v0 = 9  # reference speed

# linear system
# Compute A, B, C, D and E
A = np.array([[0, 7, 0, 0],
              [0, 0, 0, 7/3],
              [0, 0, 0, 0],
              [0, 0, 0, 0]])

B = np.array([[0, 0],
              [0, 0],
              [1, 0],
              [0, 1]])

C = np.array([[1, 0, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

D = np.array([[0, 0],
              [0, 0],
              [0, 0]])

E = np.array([[1, 0, 0, 0],
              [0, 0, 1, 0]])

# eigenvalues
# choose pcom and pobs
pobs = [-2.01, -2.02, -2.03, -2.04]
pcom = [-2, -1.01, -1.02, -1.03]

# compute KLH control
val_K = place_poles(A, B, pcom)
val_L = place_poles(A.T, C.T, pobs)

K = val_K.gain_matrix
L = val_L.gain_matrix.T
H = - np.linalg.inv(E @ np.linalg.inv(A - B @ K) @ B)

# equilibrium point
ubar = np.zeros(2)
xRbar = np.array([5, np.pi/2, 7, 0])
wbar = E@xRbar
ybar = np.array([5, 7, 0])

# define the evolution function of the regulator
def regul_evol(xr, w, y):
    #xrdot = np.zeros((4,1))
    xrdot = (A - B @ K - L @ C) @ xr + L @ (y-ybar)
    return xrdot


track = np.array([
                [-10, -12, -10, 0, 10, 20, 40, 32, 35, 30,  20,  0,   -10],
                [-5,   0,  5,  50, 60, 60, 50, 15, 5,  -10, -15, -15, -5]
                ])

#Initial conditions
x = np.array([-18, 0, np.pi/2, v0, 0])  # initial state for car
xr = np.array([0, 0, 0, 0]) # initial state for observer
u = np.array([0, 0])  # only for testing purposes
w = np.array([r0, v0])  # reference


h = 0.05  # timestep
T = np.arange(0, 40, h)
D = []  # list of distances from the car to the track at each timestep
for t in T:
    # sensors
    y = observation_func(x, track)
    D.append(y[0])
    # control
    #u =
    # updates for the car and the regulator
    # RK2 for regulator
    k1 = regul_evol(xr, w, y)
    k2 = regul_evol(xr + (h * k1), w, y)
    xr = xr + (h / 2) * (k1 + k2)
    u = -K@xr

    # RK2 for car
    k1 = car_dyn(x, u)
    k2 = car_dyn(x + (h*k1), u)
    x = x + (h/2) * (k1+k2)

    car.draw(x, y[0], track, size=150)

# plot the tracking error wrt time
# plot the control signals wrt time

#plt.show()