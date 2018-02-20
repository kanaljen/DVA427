from math import cos, sin
import numpy as np


def simulate(force, x, x_dot, theta, theta_dot):
    """ compute the next states given the force and the current states """
    g = 9.8
    cartm = 10.0
    polem = 0.1
    totm = polem + cartm
    length = 0.5
    polem_len = polem * length
    dt = 0.02
    fourthirds = 1.3333333333333

    costheta = cos(theta)
    sintheta = sin(theta)

    temp = (force + polem_len * theta_dot * theta_dot * sintheta) / totm

    thetaacc = (g * sintheta - costheta * temp) / \
        (length * (fourthirds - polem * costheta * costheta / totm))

    xacc = temp - polem_len * thetaacc * costheta / totm

    # Update the four state variables, using Euler's method.

    state = np.empty(4, 1)
    state[0] = x + dt * x_dot
    state[1] = x_dot + dt * xacc
    state[2] = theta + dt * theta_dot
    state[3] = theta_dot + dt * thetaacc

    return state


def isDead(x, ang):
    if abs(x) > 2.4:
        return False
    elif abs(ang) > 12:
        return False
    else:
        return True
