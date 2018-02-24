import numpy as np
import TSM
import matplotlib.pyplot as plt

infile = open('berlin52.tsp', 'r')

# Read instance header
Name = infile.readline().strip().split()[1]  # NAME
FileType = infile.readline().strip().split()[1]  # TYPE
Comment = infile.readline().strip().split()[1]  # COMMENT
Dimension = infile.readline().strip().split()[1]  # DIMENSION
EdgeWeightType = infile.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
infile.readline()

# Read node list
nodelist = []
N = int(Dimension)
for i in range(0, int(Dimension)):
    x, y = infile.readline().strip().split()[1:]
    nodelist.append([float(x), float(y)])

# Close input file
infile.close()

# Create array
dataset = np.array(nodelist)

# Test variables
salesmen = 200
offsprings = 20
iters = 10000


TSM = TSM.OverHead(n_cities=52, n_salesmen=salesmen, n_offsprings=offsprings)
results = TSM.test(dataset, iters)

plt.plot(results)
plt.xlabel('Iterations')
plt.ylabel('Distance')

titl = 'Smen:' + str(salesmen) + ', Ospring: ' + \
    str(offsprings) + ', Iter: ' + str(iters)
plt.title(titl)
plt.show()