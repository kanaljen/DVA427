def training(self,tset,depcol = [],rate = 0.1,target_acc = 100):
		# Check dim of input and output
		if (tset.shape[1] - len(depcol)) != len(self.ilayer.values): 
			print("Network-input size doesn't match trainingset-size")
			return 0
		elif len(depcol) != len(self.olayer.values):
			print("Network-output size doesn't match number of dependent variables")
			return 0

		# Create dependent set, from colums in depcol
		depset = np.empty([tset.shape[0],len(depcol)])
		for i in range(len(depcol)):
			depset[:,i] = tset[:,depcol[i]] 

		# Create independent set, from other columns
		inset = np.empty([tset.shape[0],tset.shape[1]-len(depcol)])
		inindex = 0
		for i in range(tset.shape[1]):
			if i in depcol:
				continue
			else:
				inset[:,inindex] = tset[:,i]
				inindex += 1

		# Create lists of weight and value delta-matrices for hidden-layers
		wdelta = []
		vdelta = []
		for i in range(len(self.hlayer)):
			wdelta.append(np.empty([self.hlayer[i].values.shape[0],self.hlayer[i].weights.shape[1]]))
			vdelta.append(np.empty([self.hlayer[i].values.shape[0],]))

		# Append weight and value delta-matrices for output
		wdelta.append(np.empty([self.olayer.values.shape[0],self.olayer.weights.shape[1]]))
		vdelta.append(np.empty([self.olayer.values.shape[0],]))
		

		# Loop samples
		for sample in range(inset.shape[0]):

			# Classify the sample
			self.classify(list(inset[sample,:]))

			# Calculating the errors
			errors = 0.5*(depset[sample] - self.olayer.values)**2
			
			# Loop outputs from classify to calculate value-delta for output-layer
			for v in range(self.olayer.values.shape[0]):
				nodevalue = self.olayer.values[v]
				# Calculate value delta for each node
				vdelta[len(vdelta)-1][v] = nodevalue*(1-nodevalue)*(depset[sample,v]-nodevalue)

			# Loop hidden layer and calculate value delta for each
			for l in range(len(self.hlayer)):
				# Loop nodes in each layer
				for n in range(self.hlayer[l].values.shape[0]):
					nodevalue = self.hlayer[l].values[n]
					# Calculate value delta for each node
					if l == (len(self.hlayer) - 1): # Last hidden-layer
						pass
						#vdelta[l][n] = nodevalue*(1-nodevalue)*self.olayer.weights[n,]
