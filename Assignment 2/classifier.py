import numpy as np


class Fuzzy_classifier(object):
	""" A classifier of iris species
	NOTE: names understood are: setosa, versicolor and virginica.
	Arg's are: x1 = sepal_length, x2 = sepal_with, x3 = petal_length, x4 = petal_width, x5 = name"""
	# TODO: Calculate degrees for all cases
	
	def __init__(self, amount_of_flowers=0):

		self.x_min = np.empty(shape=(4, 1))
		self.x_max = np.empty(shape=(4, 1))
		self.accurcy = 0
		self.iris = []
		self.short = 0
		self.middle = 0
		self.long = 0
		# attr_info determines max and min of x1 - x4. [:,0] = min, [:,1] = max
		self.attr_info = np.array([4, 2])
		# Create flowers
		for x in range(amount_of_flowers):
			self.iris.append(Flower())

	# Calculates min and max of all attributes
	def __min_max_fun(self, tset):
		for i in range(len(tset[:, 0])):
			self.x_min[i] = np.amin(tset[i, :])
			self.x_max[i] = np.amax(tset[i, :])

	def __fuzzy_set(self, i, k):
		self.iris[i].normalized_attr[k] = ((
			self.iris[i].attributes[k] - self.x_min[k]) / (self.x_max[k] - self.x_min[k]))
		self.__attr_func(self.iris[i].normalized_attr[k], i, k)
		if self.iris[i].short[k] > self.iris[i].middle[k]:
			if self.iris[i].short[k] > self.iris[i].long[k]:
				self.iris[i].dominant_attr[k] = 0
			else:
				self.iris[i].dominant_attr[k] = 2
		elif self.iris[i].middle[k] > self.iris[i].long[k]:
			self.iris[i].dominant_attr[k] = 1
		else:
			self.iris[i].dominant_attr[k] = 2


	def __attr_func(self, x, i, k):
		self.iris[i].short[k] = 1-((5/3)*x) if x < 0.6 else 0
		self.iris[i].middle[k] = (5/3)*x if x < 0.6 else 2.5-2.5*x
		self.iris[i].long[k] = 2.5*x-1.5 if x > 0.6 else 0

	def test(self, tset):
		self.__min_max_fun(tset)
		for i in range(len(tset[0])):
			for k in range(len(tset[:, 0])):
				self.iris[i].attributes[k] = tset[k, i]
				self.__fuzzy_set(i, k)
			self.iris[i].rule[0] = self.__r1(i)
			self.iris[i].rule[1] = self.__r2(i) * 0.3
			self.iris[i].rule[2] = self.__r3(i) * 10
			self.iris[i].rule[3] = self.__r4(i)
			for n in range(4):
				if self.iris[i].rule[n] == np.amax(self.iris[i].rule):
					if(n==1):
						self.iris[i].species = 1
					elif(n==2):
						self.iris[i].species = 3
					else:
						self.iris[i].species = 2

	def classify(self, samples):
		samples

	def __or_operator(x, y):
		result = max(x,y)
		return result

	def __and_operator(x, y):
		result = min(x,y)
		return result

	def __r1(self, i):
		result = min(min(min(max(self.iris[i].short[0],self.iris[i].long[0]),max(self.iris[i].middle[1],self.iris[i].long[1])),max(self.iris[i].middle[2],self.iris[i].long[2])),self.iris[i].middle[3])
		return result

	def __r2(self, i):
		result = min((max(self.iris[i].short[2],self.iris[i].middle[2])),self.iris[i].short[3])
		return result

	def __r3(self, i):
		result = min(min(max(self.iris[i].short[1],self.iris[i].long[1]),self.iris[i].long[2]),self.iris[i].long[3])
		return result

	def __r4(self, i):
		result = min(min(min(self.iris[i].middle[0],max(self.iris[i].short[1],self.iris[i].middle[1])),self.iris[i].short[2]),self.iris[i].long[3])
		return result
	"""
	def __r1(self, i):
		if self.iris[i].dominant_attr[0] == 0 or 2:
			if self.iris[i].dominant_attr[1] == 1 or 2:
				if self.iris[i].dominant_attr[2] == 1 or 2:
					if self.iris[i].dominant_attr[3] == 1:
						return self.iris[i].normalized_attr[self.iris[i].dominant_attr[0]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[1]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0

	def __r2(self, i):
		if self.iris[i].dominant_attr[2] == 0 or 1:
			if self.iris[i].dominant_attr[3] == 0:
				return self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0

	def __r3(self, i):
		if self.iris[i].dominant_attr[1] == 0 or 1:
			if self.iris[i].dominant_attr[2] == 2:
				if self.iris[i].dominant_attr[3] == 2:
					return self.iris[i].normalized_attr[self.iris[i].dominant_attr[1]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0

	def __r4(self, i):
		if self.iris[i].dominant_attr[0] == 1:
			if self.iris[i].dominant_attr[1] == 0 or 1:
				if self.iris[i].dominant_attr[2] == 0:
					if self.iris[i].dominant_attr[3] == 2:
						return self.iris[i].normalized_attr[self.iris[i].dominant_attr[0]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[1]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0
	
	def __r1(self, i):
		if self.iris[i].dominant_attr[1] == 1 or 2:
			if self.iris[i].dominant_attr[2] == 1 or 2:
				if self.iris[i].dominant_attr[3] == 1:
					return self.iris[i].normalized_attr[self.iris[i].dominant_attr[0]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[1]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0

	def __r2(self, i):
		if self.iris[i].dominant_attr[2] == 0 or 1:
			if self.iris[i].dominant_attr[3] == 0:
				return self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0

	def __r3(self, i):
		if self.iris[i].dominant_attr[1] == 0 or 1:
			if self.iris[i].dominant_attr[2] == 2:
				if self.iris[i].dominant_attr[3] == 2:
					return self.iris[i].normalized_attr[self.iris[i].dominant_attr[1]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0

	def __r4(self, i):
		if self.iris[i].dominant_attr[0] == 1:
			if self.iris[i].dominant_attr[1] == 0 or 1:
				if self.iris[i].dominant_attr[2] == 0:
					if self.iris[i].dominant_attr[3] == 2:
						return self.iris[i].normalized_attr[self.iris[i].dominant_attr[0]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[1]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[2]]*self.iris[i].normalized_attr[self.iris[i].dominant_attr[3]]
		return 0"""

class Flower(object):
	""" A layer in the neural network """

	def __init__(self, sepal_length=0, sepal_with=0, petal_length=0, petal_width=0, name=None):
		self.attributes = np.empty(shape=(4, 1)) # Holds the values of x1 - x4
		self.normalized_attr = np.empty(shape=(4, 1)) # Holds the normalized values of x1 - x4
		self.short = np.empty(shape=(4, 1)) # What is the degree of short in x1 - x4
		self.middle = np.empty(shape=(4, 1)) # Degree middle
		self.long = np.empty(shape=(4, 1))	# Degree long
		self.dominant_attr = np.empty(shape=(4, 1), dtype = int) # Tells which attr. that is dominant in x1-x4
		self.rule = np.empty(shape=(4, 1))
		self.species = 0 # What species is this flower
