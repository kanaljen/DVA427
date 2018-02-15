import numpy as np


class Fuzzy_classifier(object):
    """ A classifier of iris species
    NOTE: names understood are: setosa, versicolor and virginica.
    Arg's are: x1 = sepal_length, x2 = sepal_with,
    x3 = petal_length, x4 = petal_width, x5 = name"""
    # TODO: Calculate degrees for all cases

    def __init__(self, amount_of_flowers=0):

        self.x_min = np.empty(shape=(4, 1))
        self.x_max = np.empty(shape=(4, 1))
        self.iris = []

        # Create flowers
        for x in range(amount_of_flowers):
            self.iris.append(Flower())

    # Calculates min and max of all attributes
    def __min_max_fun(self, tset):
        # Loop columns
        for i in range(len(tset[:, 0])):
            self.x_min[i] = np.amin(tset[i, :])
            self.x_max[i] = np.amax(tset[i, :])

    def __fuzzy_set(self, i, k):
        # Normalize
        self.iris[i].normalized_attr[k] = ((
            self.iris[i].attributes[k] - self.x_min[k]) / (self.x_max[k] - self.x_min[k]))
        # Calculate short/middle/long accordning to graph
        self.__attr_func(self.iris[i].normalized_attr[k], i, k)


    def __attr_func(self, x, i, k):
        # Calculate short/middle/long accordning to graph
        self.iris[i].short[k] = 1 - ((5 / 3) * x) if x < 0.6 else 0
        self.iris[i].middle[k] = (5 / 3) * x if x < 0.6 else 2.5 - 2.5 * x
        self.iris[i].long[k] = 2.5 * x - 1.5 if x > 0.6 else 0

    def test(self, tset):
        # Get min/max of all attributes
        self.__min_max_fun(tset)
        # Loop dataset
        for i in range(len(tset[0])):

            # Loop dataset and copy attributes
            for k in range(len(tset[:, 0])):
                # COPY attributes
                self.iris[i].attributes[k] = tset[k, i]
                # Normalize and calculate short/medium/long
                self.__fuzzy_set(i, k)

            # Apply rules for all flowers
            self.iris[i].rule[0] = self.__r1(i)
            self.iris[i].rule[1] = self.__r2(i) # * 0.3
            self.iris[i].rule[2] = self.__r3(i)
            self.iris[i].rule[3] = self.__r4(i)

            # Check for flower spicies
            for n in range(4):
                if self.iris[i].rule[n] == np.amax(self.iris[i].rule):
                    if(n == 1):
                        self.iris[i].species = 1
                    elif(n == 2):
                        self.iris[i].species = 3
                    else:
                        self.iris[i].species = 2

    def __r1(self, i):
        # Max = or, min = and
        result = min(min(min(max(self.iris[i].short[0], self.iris[i].long[0]), max(self.iris[i].middle[1], self.iris[i].long[1])), max(
            self.iris[i].middle[2], self.iris[i].long[2])), self.iris[i].middle[3])
        return result

    def __r2(self, i):
        result = min(
            (max(self.iris[i].short[2], self.iris[i].middle[2])), self.iris[i].short[3])
        return result

    def __r3(self, i):
        result = min(min(max(self.iris[i].short[1], self.iris[i].long[1]),
                         self.iris[i].long[2]), self.iris[i].long[3])
        return result

    def __r4(self, i):
        result = min(min(min(self.iris[i].middle[0], max(
            self.iris[i].short[1], self.iris[i].middle[1])), self.iris[i].short[2]), self.iris[i].long[3])
        return result


class Flower(object):
    """ A layer in the neural network """

    def __init__(self, sepal_length=0, sepal_with=0, petal_length=0, petal_width=0, name=None):
        self.attributes = np.empty(shape=(4, 1))  # Holds the values of x1 - x4
        # Holds the normalized values of x1 - x4
        self.normalized_attr = np.empty(shape=(4, 1))
        # What is the degree of short in x1 - x4
        self.short = np.empty(shape=(4, 1))
        self.middle = np.empty(shape=(4, 1))  # Degree middle
        self.long = np.empty(shape=(4, 1))  # Degree long
        # Tells which attr. that is dominant in x1-x4
        self.dominant_attr = np.empty(shape=(4, 1), dtype=int)
        self.rule = np.empty(shape=(4, 1))
        self.species = 0  # What species is this flower
