import ann
import numpy as np

# Load dataset from file
dataset = np.loadtxt('titanic.dat',delimiter=',')

for t in range(dataset.shape[0]):
		dataset[t,3] = 0.75 if dataset[t,3] == 1 else 0.25

# Split dataset
setlist = np.split(dataset, [1500])



# Instance Network
net = ann.Network([3,10,10,10,1])

# Train network
net.training(setlist[0][:,0:3], setlist[0][:,3:4])


preformance = 0

# Test cases
for i in range(setlist[1].shape[0]):

	result = net.forward(setlist[1][i,0:3])

	if result >= 0.5:
		if setlist[1][i,3:4] == 0.75:
			preformance += 1
	else:
		if setlist[1][i,3:4] == 0.25:
			preformance += 1

print('Testset preformance: {:.4} %'.format((preformance/setlist[1].shape[0])*100))