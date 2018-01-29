import numpy as np

class Fuzzy_classifier(object):
    """ A classifier of iris species
    NOTE: names understood are: setosa, versicolor and virginica.
    Arg's are: x1 = sepal_length, x2 = sepal_with, x3 = petal_length, x4 = petal_width, x5 = name"""  
    # TODO: Add description

    def __init__(self, amount_of_flowers=0):

        self.accurcy = 0
        # attr_info determines max and min of x1 - x4. [:,0] = min, [:,1] = max
        self.attr_info = np.array([4,2])
        # Create flowers
        for x in range(amount_of_flowers):
            self.iris.append(Flower(sepal_length=0, sepal_with=0, petal_length=0, petal_width=0, name=None))

    # Calculates min and max of all attributes
    def __min_max_fun(self,tset):
    	for i in range(len(tset[:,0])):
    		self.x_min[i] = np.amin(tset[0,:])
    		self.x_max[i] = np.amax(tset[0,:])

    def __fuzzy_set(self,i,k):
    	self.iris[i].normalized_attr[k] = (self.attributes[k]-self.x_min[k])/(self.x_max[k]-self.x_min[k])
    
    def test(self, tset):
    	self.__min_max_fun(tset)
    	for i in range(len(tset[0])):
    		for k in range(len(tset[:,0])):
    			self.__fuzzy_set




    def classify(self, samples):
    	samples
class Flower(object):
    """ A layer in the neural network """

    def __init__(self, sepal_length=0, sepal_with=0, petal_length=0, petal_width=0, name=None):
        self.attributes = np.array([5,1])
        self.normalized_attr = np.array([4,1])
