import ann
import numpy as np


# Load dataset from file
dataset = np.loadtxt('titanic.dat', delimiter=',')

for t in range(dataset.shape[0]):
    dataset[t, 3] = 0.75 if dataset[t, 3] == 1 else 0.25

# Split dataset
setlist = np.split(dataset, [1500])


# Instance Network
net = ann.Network([3, 20, 1])

# Train network
net.training(setlist[0][:, 0:3], setlist[0][:, 3:4])


dead = 0
alive = 0
performace = 0

# Test cases
for i in range(setlist[1].shape[0]):

    result = net.forward(setlist[1][i, 0:3])

    if result >= 0.5:
        alive += 1
        if setlist[1][i, 3] == 0.75:
            performace += 1
    else:
        dead += 1
        if setlist[1][i, 3] == 0.25:
            performace += 1

print('Dead: ' + str(dead))
print('Alive: ' + str(alive))
print('Performace: ' + str(performace / 700 * 100))
