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
        """TODO"""
        #delta_weights[j-1,k,b] = n*delta_hidden[j-1,k]*t_set[i,b]  -- b blir out of bound då i_edges > n_nodes
        n = 0.1 # n defines the learning rate
        h_layers = len(self.hlayer)
        n_nodes = len(self.hlayer[0].values)-1
        i_edges = len(self.ilayer.values)
        print(t_set.shape)
        print(t_answ.shape)
        for i in range(0,len(t_set)):
            target = t_answ[i]
            #print(target)
            self.classify(t_set[i])
            #print(type(self.olayer.values[0].item(0)))
            #print(self.olayer.values[0].item(0))

            delta_output = (target-self.olayer.values)*self.olayer.values*(1-self.olayer.values)
            sum_w_delta = np.empty([h_layers,n_nodes])
            delta_hidden = np.empty([h_layers,n_nodes])
            if len(self.ilayer.values) > len(self.hlayer[0].values):
                delta_weights = np.empty([h_layers+1,n_nodes,i_edges])
            else:
                delta_weights = np.empty([h_layers+1,n_nodes,n_nodes+1])
            #print('shape',delta_weights.shape)
            """if len(self.ilayer.values) > len(self.hlayer[0].values):
                current_layer_weights = np.empty([h_layers+1,n_nodes,i_edges])
            else
                current_layer_weights = np.empty([h_layers+1,n_nodes,n_nodes])"""

            # Loop number of layers
            for j in range(len(self.hlayer)+1,0,-1):                
                if ((j == h_layers+1) & (j > 0)):
                    # Loop to get weights for output layer        
                    for a in range(0,n_nodes):
                        #print('self.hlayer[j-2].values[a]',self.hlayer[j-2].values[a])
                        delta_weights[j-1,0,a] = n*delta_output*self.hlayer[j-2].values[a]                        
                        sum_w_delta[[j-2],[a]] = delta_output*self.olayer.weights[[0],[a]]                        
                else:
                    # Loop number of nodes per hidden layer
                    for k in range(0,n_nodes):                
                        delta_hidden[[j-1],[k]] = self.hlayer[j-1].values[k]*(1-self.hlayer[j-1].values[k])*sum_w_delta[[j-1],[k]]

                        if j > 1:
                            #Loop number of incoming nodes to hidden layers
                            for b in range(0,n_nodes):
                                delta_weights[j-1,k,b] = n*delta_hidden[[j-1],[k]]*self.hlayer[j-2].values[b]
                                #self.hlayer[j].weights[[k],[b]] = n*delta_hidden[[j],[k]]*self.hlayer[j-1].values[b]
                                sum_w_delta[j-2,b] += delta_hidden[j-1,k]*self.hlayer[j-1].weights[k,b]
                        else:
                            #Loop number of incoming inputs to hidden layers
                            for b in range(1,i_edges):
                                delta_weights[j-1,k,b-1] = n*delta_hidden[j-1,k]*t_set[i,b-1]
                                #self.hlayer[j].weights[[k],[b]] = n*delta_hidden[[j],[k]]*self.hlayer[j-1].values[b]
                                #sum_w_delta[[j],[b]] = sum_w_delta[[j],[b]]+delta_hidden[[j],[k]]*self.hlayer[j].weights[b]
                                
                # Updating sum_w_delta 
                for c in range (0,n_nodes):         
                    if j > 1:
                        sum_w_delta[[j-2],[c]] = sum_w_delta[[j-2],[c]]*self.hlayer[j-2].values[c]
                    
            
            # Update weights in all layers
            for j in range(len(self.hlayer)+1,0,-1):

                for k in range(0,n_nodes): 
                    if ((j == h_layers+1) & (j > 0)):
                        self.olayer.weights[[0],[k]] = self.olayer.weights[[0],[k]]+delta_weights[j-1,0,k]
                    elif j == 1:
                        for m in range(0,i_edges): 

                            self.hlayer[j-1].weights[k,m] = self.hlayer[j-1].weights[k,m]+delta_weights[j-1,k,m]
                    else:
                        for m in range(0,n_nodes): 

                            self.hlayer[j-1].weights[k,m] = self.hlayer[j-1].weights[k,m]+delta_weights[j-1,k,m]
                    

                            
            
        E_d = (1/2)*np.power((target - self.olayer.values),2)
        return E_d     
        
    def classify(self,x):
        """x is a list to be classifyed by the network """
        print(len(x))
        print(len(self.ilayer.values))
        # Break if size of input != x
        if len(self.ilayer.values) != len(x)+1:
            print("Network-input size doesn't match argument-size")
            return 0

        # Convert input to array, save it in ilayer
        self.ilayer.values = np.array(x)

        # Loop hidden layers, for each determine previous layer 
        for i in range(len(self.hlayer)): 
            prelayer = self.ilayer.values if i == 0 else self.hlayer[i-1].values
            prelayer = np.hstack((1,prelayer))            
            #print('start')
            #print(prelayer)
            #print(len(self.hlayer[0].values))
            #print(np.transpose(prelayer).shape)
            #print(prelayer.shape)
            #print(np.transpose(self.hlayer[i].weights).shape)     
            #print(self.hlayer[i].weights.shape)       
            #print('end')
            #self.hlayer[i].values = np.matmul(prelayer,np.transpose(self.hlayer[i].weights))
            #print(prelayer.shape)
            #print(np.transpose(self.hlayer[i].weights).shape)
            self.hlayer[i].values = self.__activ_func(self.func,np.matmul(prelayer,np.transpose(self.hlayer[i].weights)))
            #self.hlayer[i].values[0] = 1
            #print(self.hlayer[i].values)
            #print(self.hlayer[i].values)

        # Determine previous layer for output
        if len(self.hlayer) != 0:
            prelayer = self.hlayer[-1].values
            prelayer = np.hstack((1,prelayer)) 
        else: 
            prelayer = self.ilayer.values
            prelayer = np.hstack((1,prelayer)) 
        #print('oprelayershape',prelayer.shape)
        #print('olayerweightsshape',np.transpose(self.olayer.weights).shape)
        # Write output
        self.olayer.values = self.__activ_func(self.func,np.matmul(prelayer,np.transpose(self.olayer.weights)))

        return self.olayer.values

class Layer(object):
    """ A layer in the neural network """

    def __init__(self, size, incedges = 0, func = None):
        self.values = np.array((size+1) *[0.])
        self.weights = np.random.rand(size,incedges+1)
        self.func = func