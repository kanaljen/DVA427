import ann
import numpy as np

# Load dataset from file
dataset = np.loadtxt('titanic.dat',delimiter=',')

# Split dataset, independent/dependent
setlist = np.split(dataset, [1500,1850])
targetlist = []

for i in range(len(setlist)):
	# Create targetlist
	targetlist.append(np.delete(setlist[i],np.s_[:3],1))

	# Rewrite target
	for t in range(targetlist[i].shape[0]):
		targetlist[i][t,0] = 0.75 if targetlist[i][t,0] == 1 else 0.25

	# Create setlist
	setlist[i] = np.delete(setlist[i],np.s_[3],1)

net = ann.Network(inodes=3,hnodes=[10,10],onodes=1,func='sig')

net.training(setlist[0],targetlist[0])
