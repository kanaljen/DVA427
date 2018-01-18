from random import uniform as uf

class Network:

	accurcy = 0

	def __init__(self, num_inputs = 1,hidden = [1],num_output = 1):
		self.ilayer = num_inputs
		self.hlayers = hidden
		self.nlayers = len(hidden)
		self.olayer = num_output

	def training(self,tset):
		"""x is the trainingset """
		pass

class NetworkNode(object):
	"""docstring for NetworkNode"""
	def __init__(self, num_output = 1):
		weights = []
		for x in range(0,num_output):
			weights.append(uf(-1,1))
		self.value = (uf(0,1),weights)
		
net = Network()
node = NetworkNode(20)

print(node.value)

print(net.training(4))
