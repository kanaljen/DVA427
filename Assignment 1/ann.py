import numpy as np
from random import uniform as uf

class Network(object):
	""" A neural network""" # TODO: Add description

	def __init__(self, inodes = 1,hnodes = [],onodes = 1,func = None):

		self.accurcy = 0
		self.hlayer = []
		self.func = func
		
		# Create input layer
		self.ilayer = Layer(size = inodes)

		# Create output layer
		if len(hnodes) > 0: incedges = hnodes[len(hnodes)-1]
		else: incedges = inodes
		self.olayer = Layer(size = onodes,incedges = incedges)

		# Create hidden layers
		for x in range(0,len(hnodes)):
			if x == 0: incedges = inodes
			else: incedges = hnodes[x-1]
			self.hlayer.append(Layer(size = hnodes[x], incedges = incedges))

	def __activ_func(self,func,vector):
		""" Activation functions for the network, called by the classify method """
		if func == 'tanh':
			return np.tanh(vector)
		elif func == 'sig':
			return 1 / (1 + np.exp(-vector))
		else:
			return vector

	def training(self,tset):
		"""tset is the trainingset """
		pass # TODO: Fix function

	def classify(self,x):
		"""x is a list to be classifyed by the network """

		# Break if size of input != x
		if len(self.ilayer.values) != len(x):
			print("Network-input size doesn't match argument-size")
			return 0

		# Convert input to array, save it in ilayer
		self.ilayer.values = np.array(x)

		# Loop hidden layers, for each determine previous layer 
		for i in range(0,len(self.hlayer)): 

			prelayer = np.transpose(self.ilayer.values) if i == 0 else np.transpose(self.hlayer[i-1].values)

			# Loop nodes in a layer
			for j in range(0,len(self.hlayer[i].values)): # Loop nodes
				self.hlayer[i].values[j] = self.__activ_func(self.func,np.dot(prelayer,self.hlayer[i].weights[j]))

		# Determine previous layer for output
		if len(self.hlayer) != 0:
			prelayer = np.transpose(self.hlayer[len(self.hlayer)-1].values) 
		else: 
			prelayer = np.transpose(self.ilayer.values)

		# Write output
		self.olayer.values = self.__activ_func(self.func,np.dot(prelayer,self.olayer.weights))

		return self.olayer.values

class Layer(object):
	""" A layer in the neural network """

	def __init__(self, size, incedges = 0, func = None):
		self.values = np.array(size *[0.])
		self.weights = np.random.rand(size,incedges)
		self.func = func
