import numpy as np

class OverHead(object):

	def __init__(self, n_cities=52, n_salesmen=10):

		self.city_matrix = np.empty(shape=(n_cities, n_cities)) # Matrix to define the distance between all cities
		self.city = []
		self.salesman = []
		self.offspring = []
		self.best_salesmen = []

		for i in range(n_cities):
			self.city.append(City()) # Vector of the cities

		for i in range(n_salesmen):
			self.salesman.append(Salesman(n_cities))

		for i in range(n_salesmen-2):
			self.offspring.append(Salesman(n_cities))

	def distance_two_cities(self,i,k):
		#Returns the distance between two cities a and b
		distance = np.sqrt(np.square(self.city[k].x-self.city[i].x)+np.square(self.city[k].y-self.city[i].y)) 
		return distance

	def fitness_evaluator(self):
		# Returns a vector with the indexes of the best salesmen. Best salesman on index 0
		#self.best_salesmen = np.empty(shape=(1, 1),dtype=int)
		self.best_salesmen = np.array([0])
		#self.best_salesmen[0] = 0
		for i in range(1,len(self.salesman)):
			for k in range(len(self.salesman)):
				if k >= i:
					self.best_salesmen = np.insert(self.best_salesmen,k,i)
					break
				elif self.salesman[i].tot_dist < self.salesman[self.best_salesmen[k]].tot_dist:
					self.best_salesmen = np.insert(self.best_salesmen,k,i)
					break


	def add_cities(self, c_set):
		# Adding all cities from c_set
		for i in range(len(c_set[:,0])):
			# Loop through all cities
			self.city[i].x = c_set[i,0]
			self.city[i].y = c_set[i,1]
			self.city_matrix[i,i] = 0
			for k in range(i):
				# Define the distance between all cities				
				self.city_matrix[i,k] = self.distance_two_cities(i,k)
				self.city_matrix[k,i] = self.city_matrix[i,k] # Matrix is symmetric

	def create_salesmen(self):

		for i in range(len(self.salesman)):
			for k in range(len(self.salesman[i].route)):
				self.salesman[i].tot_dist = self.salesman[i].tot_dist + self.city_matrix[self.salesman[i].route[k-1],self.salesman[i].route[k]]

	def crossover(self,a,b):

		self.salesman[0].route = self.salesman[a].route
		self.salesman[1].route = self.salesman[b].route
		#print('salsesman[0]route len=',len(self.salesman[0].route))

		sequence_length = 10

		for i in range(len(self.offspring)):
			self.offspring[i] = self.salesman[np.remainder(i,2)] # Copies a route from parent 1
			sequence_start = np.random.randint(1,len(self.salesman[i].route)-sequence_length)	
			#print('len salesman[i].route=',len(self.salesman[i].route))
			#print('sequence start=',sequence_start)		
			sequence_array = np.empty(shape=(sequence_length,1))
			index_delete = np.empty(shape=(sequence_length,1))
			index = 0
			for j in range(sequence_length):
				# Saves a sequence from parent 2 and stores it in a temporary vector
				sequence_array[j] = self.salesman[np.remainder(i+1,2)].route[sequence_start+j]
			for j in range(len(self.salesman[i].route)):
				# Checks which cities in the route that is also in the sequence from parent 2
				if np.any(sequence_array==self.offspring[i].route[j]):
					index_delete[index] = j
					index+=1
			# Delete the duplicate cities before adding them
			#print('delete_index=',index_delete)
			#print('före delete',self.offspring[i].route)
			self.offspring[i].route = np.delete(self.offspring[i].route,index_delete)
			#print('efter delete',self.offspring[i].route)
			for k in range(sequence_length):
				# Add the sequence from parent 2 to the offspring
				self.offspring[i].route = np.insert(self.offspring[i].route,sequence_start+k,sequence_array[k])

		for i in range(len(self.offspring)):
			self.salesman[i+2] = self.offspring[i]

	def test(self,c_set):
		self.add_cities(c_set)
		self.create_salesmen()

		for i in range(10):
			self.fitness_evaluator()
			self.crossover(self.best_salesmen[0],self.best_salesmen[1])
			#print(self.best_salesmen[0])
			print(self.salesman[self.best_salesmen[0]].tot_dist)



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