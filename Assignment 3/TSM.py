class OverHead(object):

	def __init__(self, n_cities=52, n_salesmen=10):

		self.city_matrix = np.empty(shape=(n_cities, n_cities)) # Matrix to define the distance between all cities
		self.city = []
		self.salesman = []

		for i in range(n_cities):
			self.city.append(City()) # Vector of the cities

		for i in range(n_salesmen):
			self.salesman.append(Salesman(n_cities))

	def add_cities(self, c_set):
		# Adding all cities from c_set
		for i in range(c_set[0]):
			# Loop through all cities
			self.city[i] = c_set[i]
			self.city_matrix[i,i] = 0
			for k in range(i):
				# Define the distance between all cities				
				self.city_matrix[i,k] = distance_two_cities(self.city[i],self.city[k])
				self.city_matrix[k,i] = self.city_matrix[i,k] # Matrix is symmetric

	def distance_two_cities(a,b):
		#Returns the distance between two cities a and b
		distance = np.sqrt(np.square(b.x-a.x)+np.square(b.y-a.y)) 
		return distance

	def create_salesmen(self):

		for i in range(len(self.salesman[:,0])):
			for k in range(len(self.route)):
				self.salesman[i].tot_dist = self.salesman[i].tot_dist + self.city_matrix[self.salesman[i].route[k-1],self.salesman[i].route[k]]

class City(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

class Salesman(object):

	def __init__(self, n_cities):
		self.route = np.arange(1,n_cities)
		np.random.shuffle(self.route)
		self.route = np.append(self.route,0)
		self.route = np.insert(self.route,0,0)
		self.tot_dist = 0