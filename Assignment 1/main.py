import ann
import numpy as np

# Load dataset from file
dataset = np.loadtxt('titanic.dat',delimiter=',')

for t in range(dataset.shape[0]):
		dataset[t,3] = 0.75 if dataset[t,3] == 1 else 0.25
# Split dataset, independent/dependent
setlist = np.split(dataset, [1500,1850])

"""
targetlist = []

for i in range(len(setlist)):
	# Create targetlist
	targetlist.append(np.delete(setlist[i],np.s_[:3],1))

	# Rewrite target
	for t in range(targetlist[i].shape[0]):
		targetlist[i][t,0] = 0.75 if targetlist[i][t,0] == 1 else 0.25

	# Create setlist
	setlist[i] = np.delete(setlist[i],np.s_[3],1)

"""

# Instance Network
net = ann.Network(inodes=3,hnodes=[10,10,10,10],onodes=1,func='sig')

# Train network

net.training(tset = setlist[0], depcol=[3])


preformance = 0

# Test cases
for i in range(setlist[1].shape[0]):

	result = net.classify(setlist[1][i,:])

	if result >= 0.5:
		if targetlist[1].item(i) == 0.75:
			preformance += 1
	else:
		if targetlist[1].item(i) == 0.25:
			preformance += 1

print('Testset preformance: {:.4} %'.format((preformance/setlist[1].shape[0])*100))