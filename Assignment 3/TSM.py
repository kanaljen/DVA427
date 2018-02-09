import numpy as np


class OverHead(object):

    def __init__(self, n_cities=52, n_salesmen=10):

        # Matrix to define the distance between all cities
        self.city_matrix = np.empty(shape=(n_cities, n_cities))
        self.city = []
        self.salesman = []
        self.offspring = []
        self.best_salesmen = []

        for i in range(n_cities):
            self.city.append(City())  # Vector of the cities

        for i in range(n_salesmen):
            self.salesman.append(Salesman(n_cities))

        for i in range(n_salesmen - 2):
            self.offspring.append(Salesman(n_cities))

    def distance_two_cities(self, i, k):
        # Returns the distance between two cities a and b
        distance = np.sqrt(np.square(
            self.city[k].x - self.city[i].x) + np.square(self.city[k].y - self.city[i].y))
        return distance

    def fitness_evaluator(self):
        # Returns a vector with the indexes of the best salesmen. Best salesman on index 0
        # Updates the distance route for every salesman

        self.update_salesmen()

        for i in range(len(self.salesman)):

            if i == 0:
                self.best_salesmen = np.array([0])
                self.best_salesmen[0] = 0
            else:
                for k in range(len(self.salesman)):
                    if k >= i:
                        self.best_salesmen = np.insert(
                            self.best_salesmen, k, i)
                        break
                    elif self.salesman[i].tot_dist < self.salesman[self.best_salesmen[k]].tot_dist:
                        self.best_salesmen = np.insert(
                            self.best_salesmen, k, i)
                        break

    def add_cities(self, c_set):
        # Adding all cities from c_set
        for i in range(len(c_set[:, 0])):
            # Loop through all cities
            self.city[i].x = c_set[i, 0]
            self.city[i].y = c_set[i, 1]
            self.city_matrix[i, i] = 0
            for k in range(i):
                # Define the distance between all cities
                self.city_matrix[i, k] = self.distance_two_cities(i, k)
                # Matrix is symmetric
                self.city_matrix[k, i] = self.city_matrix[i, k]

    def update_salesmen(self):
        # Updates the route distance for every salesman
        for i in range(len(self.salesman)):
            self.salesman[i].tot_dist = 0
            for k in range(len(self.salesman[i].route)):
                self.salesman[i].tot_dist = self.salesman[i].tot_dist + \
                    self.city_matrix[self.salesman[i].route[k - 1],
                                     self.salesman[i].route[k]]

    def crossover(self, a, b):

        self.salesman[0].route = np.copy(self.salesman[a].route)
        self.salesman[1].route = np.copy(self.salesman[b].route)

        sequence_length = 10

        for i in range(len(self.offspring)):
            self.offspring[i].route = np.copy(
                self.salesman[np.remainder(i, 2)].route)  # Copies a route from parent 1

            sequence_start = np.random.randint(
                1, len(self.salesman[i].route) - sequence_length)

            sequence_array = np.empty(shape=(sequence_length, 1))
            index_delete = np.zeros(sequence_length)

            index = 0
            for j in range(sequence_length):
                # Saves a sequence from parent 2 and stores it in a temporary vector
                sequence_array[j] = self.salesman[np.remainder(
                    i + 1, 2)].route[sequence_start + j]

            for k in range(len(self.salesman[i].route)):
                # Checks which cities in the route that is also in the sequence from parent 2
                if np.any(sequence_array == self.offspring[i].route[k]):

                    index_delete[index] = k

                    index += 1

            # Delete the duplicate cities before adding them

            self.offspring[i].route = np.delete(
                self.offspring[i].route, index_delete)

            for m in range(sequence_length):
                # Add the sequence from parent 2 to the offspring
                self.offspring[i].route = np.insert(
                    self.offspring[i].route, sequence_start + m, sequence_array[m])

            self.salesman[i + 2].route = np.copy(self.offspring[i].route)

    def mutation(self, n_swaps):

        # Mutation will occur up to n times
        for k in range(4, len(self.salesman)):
            if k < len(self.salesman) / 2:
                r_swaps = np.random.randint(n_swaps)
            else:
                r_swaps = np.random.randint(len(self.city))

            for i in range(r_swaps):
                a_swap = np.random.randint(1, len(self.salesman[0].route) - 1)
                b_swap = np.random.randint(1, len(self.salesman[0].route) - 1)
                while a_swap == b_swap:
                    b_swap = np.random.randint(
                        1, len(self.salesman[0].route) - 1)
                temp_a = self.salesman[k].route[a_swap]
                temp_b = self.salesman[k].route[b_swap]

                if b_swap > a_swap:

                    self.salesman[k].route = np.delete(
                        self.salesman[k].route, a_swap)
                    self.salesman[k].route = np.delete(
                        self.salesman[k].route, b_swap - 1)
                    self.salesman[k].route = np.insert(
                        self.salesman[k].route, a_swap, temp_b)
                    self.salesman[k].route = np.insert(
                        self.salesman[k].route, b_swap, temp_a)
                else:

                    self.salesman[k].route = np.delete(
                        self.salesman[k].route, b_swap)
                    self.salesman[k].route = np.delete(
                        self.salesman[k].route, a_swap - 1)
                    self.salesman[k].route = np.insert(
                        self.salesman[k].route, b_swap, temp_a)
                    self.salesman[k].route = np.insert(
                        self.salesman[k].route, a_swap, temp_b)

    def test(self, c_set, iter=100, swaps=20):
        self.add_cities(c_set)
        self.fitness_evaluator()

        results = []

        for i in range(iter):
            self.crossover(self.best_salesmen[0], self.best_salesmen[1])
            self.mutation(n_swaps=swaps)
            self.fitness_evaluator()
            print(i, self.salesman[self.best_salesmen[0]].tot_dist)
            results.append(self.salesman[self.best_salesmen[0]].tot_dist)

        return results


class City(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Salesman(object):

    def __init__(self, n_cities):
        self.route = np.arange(1, n_cities)
        np.random.shuffle(self.route)
        self.route = np.append(self.route, 0)
        self.route = np.insert(self.route, 0, 0)
        self.tot_dist = 0
