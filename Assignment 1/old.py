import numpy as np
from random import uniform as uf


class Network(object):
    """ A neural network class with a sigmoid activation-function"""

    def __init__(self, inodes=1, hnodes=[], onodes=1):

        self.accurcy = 0
        self.hlayer = []

        # Create input layer
        self.ilayer = Layer(inodes,0)

        # Create output layer
        incedges = hnodes[-1] if len(hnodes) > 0 else len(self.ilayer.values)
        self.olayer = Layer(size=onodes, incedges=incedges)

        # Create hidden layers
        for x in range(0, len(hnodes)):
            incedges = len(self.ilayer.values) if x == 0 else hnodes[x - 1]
            self.hlayer.append(Layer(size=hnodes[x], incedges=incedges))

        self.noh = len(self.hlayer) # Number of Hidden-layers

    def sigmoid(self, vector):
        """ Sigmoid activation-function """

        return 1 / (1 + np.exp(-vector))

    def training(self, train_set,target_set,rate=0.1):
        """ Training by backpropagation """



        # Loop training-set
        for case in range(train_set.shape[0]):

            # Create matrices for storing changes
            ndelta = (self.noh + 2) * [0]
            wdelta = (self.noh + 2) * [0]

            # Store layers in list
            layers = [self.ilayer]

            for i in range(self.noh):
                layers.append(self.hlayer[i])

            layers.append(self.olayer)

            # Loop layers
            for l in range(len(layers)-1,0,-1):

                output = self.forward(train_set[case])
                target = target_set[case]

                # Output-layer
                if l == len(layers)-1:

                    # Calculate node-delta
                    values = self.olayer.values
                    node_delta = np.matrix(values * (1 - values)  * (target - output))
                    print(node_delta.shape)
                    ndelta[-1] = node_delta

                    # Calculte weight-delta
                    weight_delta = rate * np.matmul(np.transpose(node_delta),np.matrix(layers[l-1].values))
                    print(weight_delta)
                    

                # Hidden-layers
                else:

                    # Calculate node-delta
                    # backpro = np.dot(ndelta[l+1],layers[l+1].weights)
                    # node_delta = np.matrix(values * (1 - values) * backpro)
                    ndelta[l] = node_delta

                    # Calculte weight-delta
            


                    



        

    def forward(self, input):
        """ The Forward Pass through the network with current weights"""

        # Break if size of input != network-input
        if len(self.ilayer.values) != input.shape[0]:
            print("(forward): input doesn't match argument")
            return 0

        self.ilayer.values = input

        # Loop hidden layers
        for i in range(0, self.noh):

            # Determine prevoius layer as prelayer
            prelayer = input if i == 0 else self.hlayer[i - 1].values

            # Calculate values
            values = np.matmul(prelayer, np.transpose(self.hlayer[i].weights)) + self.hlayer[i].bias
            self.hlayer[i].values = self.sigmoid(values)

        # Determine previous layer for output
        prelayer = self.hlayer[-1].values if self.noh != 0 else input

        # Calculate output-values
        values = np.matmul(prelayer, np.transpose(self.olayer.weights)) + self.olayer.bias
        self.olayer.values = self.sigmoid(values)

        # Return output
        return self.olayer.values


class Layer(object):
    """ A layer in the neural network """

    def __init__(self, size, incedges):
        self.values = np.empty(size,dtype='float64')
        self.bias = np.random.rand(size)
        self.weights = np.random.rand(size, incedges)
