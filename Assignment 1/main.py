import ann
import numpy as np

# Load dataset from file
dataset = np.loadtxt('titanic.dat',delimiter=',')

# Split data set
setlist = np.split(dataset, [1500,1850])
training_set = setlist[0]
test_set = setlist[1]
validation_set = setlist[2]

# Rewrite target values in trainingset
for x in range(training_set.shape[0]):
	training_set[x,3] = 0.75 if training_set[x,3] == 1 else 0.25

# Create network
net = ann.Network(inodes = 3,hnodes = [10,10],onodes = 1,func = 'sig')

# Train network
net.training(training_set,[3])

# print(training_set[:,3])