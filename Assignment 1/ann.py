import numpy as np
from random import uniform as uf

class Network:
	"""docstring for Network""" # TODO: Add description

	def __init__(self, inodes = 1,hnodes = [],onodes = 1):
		# TODO: To be able to choose normalization func/layer
		self.accurcy = 0
		self.ilayer = []
		self.hlayer = []
		self.olayer = []
		
		# Create input layer
		if len(hnodes) > 0: oedges = hnodes[0]
		else: oedges = onodes
		self.ilayer = self.__build_layer(inodes,oedges,None)

		# Create output layer
		self.olayer = self.__build_layer(onodes,0,None)

		# Create hidden layers
		for x in range(0,len(hnodes)):
			if x == (len(hnodes) - 1): oedges = onodes
			else: oedges = hnodes[x+1]
			self.hlayer.append(self.__build_layer(hnodes[x],oedges,None))

	def __build_layer(self,nodes,oedges,func):
		layer = []
		for x in range(0,nodes): layer.append(NetworkNode(oedges = oedges,func = func))
		return layer

	def training(self,tset):
		"""tset is the trainingset """
		pass # TODO: Fix function

	def classify(self,x):
		"""x is the array to be classifyed by the network """
		if len(self.ilayer) != len(x):
			print("Network-input size doesn't match argument size")
			return 0

class NetworkNode(object):
	""" One of the nodes in the ANN
		The node takes inputs by the 'input' methode,
		it outputs a normilized value with the 'output' method
		and resets it's value with 'reset'"""

	def __init__(self, oedges,func):
		""" num_outputs is the number of outputnodes in the next layer
			func is the normalization function """
		self.weights = np.array([])
		self.value = 0
		self.__normal_func = func

		# Fill node with random weights
		for x in range(0,oedges):
			self.weights = np.append(self.weights,uf(-1,1))

	def input(self,input):
		""" Takes one input and add it to the current value """
		self.value += input

	def output(self):
		""" Return sum of all inputs after normalization """
		if self.__normal_func == None:
			return self.value
		elif self.__normal_func == 'Some other function':
			# Normalize with function and return
			normalized = self.__normal_func
			return normalized
		else: return 0
		# TODO: Add normalization functions

	def reset(self):
		self.value = 0

