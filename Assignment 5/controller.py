from pendal import *


class Cart(object):
    """docstring for Cart"""

    def __init__(self):
        self.state = [0.0,0.0,0.0,0.0]

    def update(self, force):
        """ compute the next states given the force and the current states """

        # Store current state in calculation vars
        x = self.state[0]
        x_dot = self.state[1]
        theta = self.state[2]
        theta_dot = self.state[3]

        # Create constatnts
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

        # Calculate stuff
        temp = (force + polem_len * theta_dot * theta_dot * sintheta) / totm

        thetaacc = (g * sintheta - costheta * temp) / \
            (length * (fourthirds - polem * costheta * costheta / totm))

        xacc = temp - polem_len * thetaacc * costheta / totm

        # Update the four state variables, using Euler's method.

        self.state[0] = x + dt * x_dot
        self.state[1] = x_dot + dt * xacc
        self.state[2] = theta + dt * theta_dot
        self.state[3] = theta_dot + dt * thetaacc

    def stillAlive(self):
        if abs(self.state[0]) > 2.4:
            return False
        elif abs(self.state[2]) > 12.0:
            return False
        else:
            return True
