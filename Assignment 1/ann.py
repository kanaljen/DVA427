import numpy as np
from random import uniform as uf


class Network(object):
    """ A neural network"""  # TODO: Add description

    def __init__(self, inodes=1, hnodes=[], onodes=1, func=None):

        self.accurcy = 0
        self.hlayer = []
        self.func = func

        # Create input layer
        self.ilayer = Layer(size=inodes)

        # Create output layer
        if len(hnodes) > 0:
            incedges = hnodes[len(hnodes) - 1]
        else:
            incedges = inodes
        self.olayer = Layer(size=onodes, incedges=incedges)

        # Create hidden layers
        for x in range(0, len(hnodes)):
            if x == 0:
                incedges = inodes
            else:
                incedges = hnodes[x - 1]
            self.hlayer.append(Layer(size=hnodes[x], incedges=incedges))

    def __activ_func(self, func, vector):
        """ Activation functions for the network, called by the classify method """
        if func == 'tanh':
            return np.tanh(vector)
        elif func == 'sig':
            return 1 / (1 + np.exp(-vector))
        else:
            return vector

    def training(self, tset, depcol=[], rate=0.1, target_acc=100):
        # Check dim of input and output
        if (tset.shape[1] - len(depcol)) != len(self.ilayer.values):
            print("Network-input size doesn't match trainingset-size")
            return 0
        elif len(depcol) != len(self.olayer.values):
            print("Network-output size doesn't match number of dependent variables")
            return 0

        # Create dependent set, from colums in depcol
        depset = np.empty([tset.shape[0], len(depcol)])
        for i in range(len(depcol)):
            depset[:, i] = tset[:, depcol[i]]

        # Create independent set, from other columns
        inset = np.empty([tset.shape[0], tset.shape[1] - len(depcol)])
        inindex = 0
        for i in range(tset.shape[1]):
            if i in depcol:
                continue
            else:
                inset[:, inindex] = tset[:, i]
                inindex += 1

        # Create lists of weight and value delta-matrices for hidden-layers
        # First indexes 
        wdelta = []
        vdelta = []
        for i in range(len(self.hlayer)):
            wdelta.append(np.empty([self.hlayer[i].values.shape[0], self.hlayer[i].weights.shape[1]]))
            vdelta.append(np.empty([self.hlayer[i].values.shape[0], ]))

        # Append weight and value delta-matrices for output
        wdelta.append(np.empty([self.olayer.values.shape[0], self.olayer.weights.shape[1]]))
        vdelta.append(np.empty([self.olayer.values.shape[0], ]))

        # Loop samples
        for sample in range(inset.shape[0]):

            # Classify the sample
            print(self.classify(inset[sample, :]))

            # Loop outputs from classify to calculate value-delta for output-layer
            for v in range(self.olayer.values.shape[0]):
                nodevalue = self.olayer.values[v]
                # Calculate value delta for each node
                vdelta[len(vdelta) - 1][v] = nodevalue * \
                    (1 - nodevalue) * (depset[sample, v] - nodevalue)

            # Loop hidden layer and calculate value delta for each
            for l in range(len(self.hlayer)):
                # Loop nodes in each layer
                for n in range(self.hlayer[l].values.shape[0]):
                    nodevalue = self.hlayer[l].values[n]
                    # Calculate value delta for each node
                    if l == (len(self.hlayer) - 1):  # Last hidden-layer
                        pass
                        #vdelta[l][n] = nodevalue*(1-nodevalue)*self.olayer.weights[n,]

    def classify(self, x):
        """x is a list to be classifyed by the network """

        # Break if size of input != x
        if len(self.ilayer.values) != len(x):
            print("Network-input size doesn't match argument-size")
            return 0

        # Convert input to array, save it in ilayer
        self.ilayer.values = np.array(x)

        # Loop hidden layers, for each determine previous layer
        for i in range(0, len(self.hlayer)):
            prelayer = self.ilayer.values if i == 0 else self.hlayer[i - 1].values
            self.hlayer[i].values = np.matmul(
                prelayer, np.transpose(self.hlayer[i].weights))

        # Determine previous layer for output
        prelayer = self.hlayer[-1].values if len(
            self.hlayer) != 0 else self.ilayer.values

        # Write output
        self.olayer.values = self.__activ_func(
            self.func, np.matmul(prelayer, np.transpose(self.olayer.weights)))

        return self.olayer.values


class Layer(object):
    """ A layer in the neural network """

    def __init__(self, size, incedges=0, func=None):
        self.values = np.array(size * [0.])
        self.weights = np.random.rand(size, incedges)
        self.func = func
