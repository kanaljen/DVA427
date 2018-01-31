import numpy as np


class Network(object):
    """docstring for Network"""

    def __init__(self, nodes):

        self.X = []
        self.W = []
        self.accuracy = 0

        for n in range(len(nodes)):

            self.X.append(np.empty(nodes[n]))
            if n > 0:
                self.W.append(np.random.rand(nodes[n], nodes[n - 1]))
            else:
                self.W.append(0)

    def sigmoid(self, vector):
        """ Sigmoid activation function """

        return 1 / (1 + np.exp(-vector))

    def forward(self, input):
        """ Feed input forward in the network """

        self.X[0] = input

        for layer in range(1, len(self.X)):

            self.X[layer] = self.sigmoid(
                np.matmul(self.X[layer - 1], np.transpose(self.W[layer])))

        return self.X[-1]

    def training(self, train_set, target_set, rate=0.1):
        """ Train the waights by backpropagation (online-training) """

        dX = []
        dW = []

        for n in range(len(self.X)):

            if n == 0:
                dX.append(0)
                dW.append(0)
            else:
            	dX.append(np.empty(self.X[n].shape[0]))
            	dW.append(np.empty([self.X[n].shape[0], self.X[n - 1].shape[0]]))

        # Loop samples/rows in trainingset
        for sample in range(train_set.shape[0]):

            # Feed sample forward
            netout = self.forward(train_set[sample])
            target = target_set[sample]

            # Loop layers, exept input
            for layer in range(len(self.X) - 1, 0, -1):

                if layer == len(self.X) - 1:
                	dX[layer] = netout * (1 - netout) * (target - netout)

                else:

                	backpro = np.dot(dX[layer + 1], self.W[layer + 1])
                	dX[layer] = self.X[layer] * (1 - self.X[layer]) * backpro

                dW[layer] = rate * np.matmul(np.transpose(np.matrix(dX[layer])),np.matrix(self.X[layer - 1]))

        	# Loop layers, change weights
            for layer in range(1,len(self.X)):
                self.W[layer] += dW[layer]

            E = 0.5 * ( (target_set[sample] - netout)**2)
            Etot = np.sum(E)
          
            print(Etot)


