import numpy as np

fname = 'city.txt'
dt = np.dtype('str, str, uint8')

dataset = np.loadtxt(fname, dtype='str', skiprows=3)

print(dataset[1].shape)
