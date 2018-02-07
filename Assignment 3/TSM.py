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
		# Updates the distance route for every salesman
		self.update_salesmen()
		#self.best_salesmen = np.empty(shape=(1, 1),dtype=int)
		#print('salesmen dist:',self.salesman[0].tot_dist)
		for i in range(len(self.salesman)):
			#print('salesmen dist:',self.salesman[i].tot_dist)
			if i == 0:
				self.best_salesmen = np.array([0])
				self.best_salesmen[0] = 0
			else:
				for k in range(len(self.salesman)):
					if k >= i:
						self.best_salesmen = np.insert(self.best_salesmen,k,i)
						break
					elif self.salesman[i].tot_dist < self.salesman[self.best_salesmen[k]].tot_dist:
						self.best_salesmen = np.insert(self.best_salesmen,k,i)
						break
			if not len(self.salesman[i].route) == 53:
				print('salesman:',i,'not unique')


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

	def update_salesmen(self):
		# Updates the route distance for every salesman
		for i in range(len(self.salesman)):
			self.salesman[i].tot_dist = 0
			for k in range(len(self.salesman[i].route)):
				self.salesman[i].tot_dist = self.salesman[i].tot_dist + self.city_matrix[self.salesman[i].route[k-1],self.salesman[i].route[k]]

	def crossover(self,a,b):
		#print('CROSSOVER START')
		self.salesman[0].route = np.copy(self.salesman[a].route)
		self.salesman[1].route = np.copy(self.salesman[b].route)
		#print('salesman',0,'=',self.salesman[0].route)
		#print('salesman',0,'=',self.salesman[0].tot_dist)
		#print('salesman',1,'=',self.salesman[1].tot_dist)
		#print('salsesman[0]route len=',len(self.salesman[0].route))
		#print('salesman 0=',self.salesman[0].route)
		#print('salesman 1=',self.salesman[1].route)
		test_array = np.arange(52)

		sequence_length = 10

		for i in range(len(self.offspring)):
			self.offspring[i].route = np.copy(self.salesman[np.remainder(i,2)].route) # Copies a route from parent 1
			#test2_array = np.sort(self.offspring[i].route)
			#test2_array = np.delete(test2_array,0)
			#print('test2_array')
			#if not np.array_equal(test2_array,test_array):
				#print('BEFORE CROSSOVER: salesman:',i+2,'note unique')
			sequence_start = np.random.randint(1,len(self.salesman[i].route)-sequence_length)	
			#print('offspring innan',i,'=',self.offspring[i].route)
			#print('sequence_start=',sequence_start)

			#print('len salesman[i].route=',len(self.salesman[i].route))
			#print('sequence start=',sequence_start)		
			sequence_array = np.empty(shape=(sequence_length,1))
			index_delete = np.zeros(sequence_length)
			#print('new index array = ',index_delete)
			index = 0
			for j in range(sequence_length):
				# Saves a sequence from parent 2 and stores it in a temporary vector
				sequence_array[j] = self.salesman[np.remainder(i+1,2)].route[sequence_start+j]
			#print(sequence_array)
			for k in range(len(self.salesman[i].route)):
				# Checks which cities in the route that is also in the sequence from parent 2
				if np.any(sequence_array==self.offspring[i].route[k]):	
					#print('want to remove number: ',self.offspring[i].route[k])				
					index_delete[index] = k
					#print('index',index,index_delete)
					#print('sequence array',sequence_array)
					#print('offspring route',self.offspring[i].route)
					index+=1
			
			#print('index_delete',index_delete)
			# Delete the duplicate cities before adding them
			#print('delete_index=',index_delete)
			#print('före delete',self.offspring[i].route)
			self.offspring[i].route = np.delete(self.offspring[i].route,index_delete)
			#print('efter delete',self.offspring[i].route)
			for m in range(sequence_length):
				# Add the sequence from parent 2 to the offspring
				self.offspring[i].route = np.insert(self.offspring[i].route,sequence_start+m,sequence_array[m])
			#print('salesman MITT I',0,'=',self.salesman[0].route)
			#print('offspring',i,'=',self.offspring[i].route)
			#print('sequence_array',i,'=',sequence_array)
			self.salesman[i+2].route = np.copy(self.offspring[i].route)
			#test2_array = np.sort(self.salesman[i+2].route)
			#test2_array = np.delete(test2_array,0)
			#if not np.array_equal(test2_array,test_array):
				#print('AFTER CROSSOVER: salesman:',i+2,'note unique')
		#print('salesman',0,'=',self.salesman[0].route)
		#print('salesman',0,'=',self.salesman[0].tot_dist)
		#print('salesman',1,'=',self.salesman[1].tot_dist)
		#print('CROSSOVER SLUT')

	def mutation(self,n_swaps):
		#print('MUTATION START')
		test_array = np.arange(52)
		# Mutation will occur up to n times		
		for k in range(2,len(self.salesman)):
			#test2_array = np.sort(self.salesman[k].route)
			#test2_array = np.delete(test2_array,0)
			#print('test2_array')
			#if not np.array_equal(test2_array,test_array):
				#print('BEOFE MUTATION: salesman:',k,'note unique')	
			r_swaps = np.random.randint(n_swaps)
			for i in range(r_swaps):
				a_swap = np.random.randint(1,len(self.salesman[0].route)-1)
				b_swap = np.random.randint(1,len(self.salesman[0].route)-1)
				while a_swap == b_swap:
					b_swap = np.random.randint(1,len(self.salesman[0].route)-1)
				temp_a = self.salesman[k].route[a_swap]
				temp_b = self.salesman[k].route[b_swap]
				#print('salesman innan mutation',self.salesman[k].route)				
				if b_swap > a_swap:
					#print('b_swap > a_swap')
					self.salesman[k].route = np.delete(self.salesman[k].route,a_swap)
					self.salesman[k].route = np.delete(self.salesman[k].route,b_swap-1)				
					self.salesman[k].route = np.insert(self.salesman[k].route,a_swap,temp_b)
					self.salesman[k].route = np.insert(self.salesman[k].route,b_swap,temp_a)
				else:
					#print('a_swap > b_swap')
					self.salesman[k].route = np.delete(self.salesman[k].route,b_swap)
					self.salesman[k].route = np.delete(self.salesman[k].route,a_swap-1)	
					self.salesman[k].route = np.insert(self.salesman[k].route,b_swap,temp_a)
					self.salesman[k].route = np.insert(self.salesman[k].route,a_swap,temp_b)
				#print('salesman efter mutation',self.salesman[k].route)
			#test2_array = np.sort(self.salesman[k].route)
			#test2_array = np.delete(test2_array,0)
			#print('test2_array')
			#if not np.array_equal(test2_array,test_array):
				#print('AFTER MUTATION: salesman:',k,'note unique',self.salesman[k].route)	
			#if not len(self.salesman[k].route) == 53:
				#print('salesman:',k,'note unique')

	def test(self,c_set):
		self.add_cities(c_set)

		for i in range(100000):
			self.fitness_evaluator()
			self.crossover(self.best_salesmen[0],self.best_salesmen[1])
			self.mutation(n_swaps=20)
			#print('salesman',0,'=',self.salesman[0].tot_dist)
			#print('salesman',1,'=',self.salesman[1].tot_dist)
			#print('MUTATION SLUT')
			self.update_salesmen()
			#print('salesman',0,'=',self.salesman[0].tot_dist)
			#print('salesman',1,'=',self.salesman[1].tot_dist)
			#print('UPDATED SLUT')
			#print(self.best_salesmen[0])
			self.fitness_evaluator()
			print(self.salesman[self.best_salesmen[0]].tot_dist)
			#for j in range(10):
				#print(self.salesman[j].tot_dist)



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