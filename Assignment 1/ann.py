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
	def training(self,t_set,t_answ):
    	"""TODO
   	 Nollställa alla värden på sum_w_delta[,] efter varje classify
   	 Hur blir det vid input layer?
   	 Hur fungerar mina loopar?
  	  """
   	n = 0.1 # n defines the learning rate
    
   	for i in range(0,len(t_set-700)):
     	if t_answ[i] == 1:
            target = 0.75
        else:
            target = 0.25
        
        self.olayer.values = classify(t_set)
        delta_output = (target-self.olayer.values) * self.olayer.values * (1 - self.olayer.values)
        
        # Loop number of hidden layers
        for j in range(1,0):                
            
        # Loop to get weights for output layer        
            if j == 1:
                for a in range(0,2):
                    self.olayer.weights[a] = n*delta_output*self.hlayer[j-1].values[a]
                    #sum_w_delta[j+1,a] = delta_output*(np.sum(self.olayer.weights))
                
            # Loop number of nodes per hidden layer
            for k in range(2,0):                
                delta_hidden[j,k] = self.hlayer[j].values[k]*(1-self.hlayer[j].values[k])*sum_w_delta[j+1,k]
                
                #loop number of incoming nodes to hidden layers
                for b in range(0,2):
                    if j > 0:
                        self.hlayer[j].weights[b] = n*delta_hidden[j,k]*self.hlayer[j-1].values[b]
                        sum_w_delta[j,b] = sum_w_delta[j,b]+delta_hidden[j,k]*self.hlayer[j].weights[b]
                
        
            
            

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
