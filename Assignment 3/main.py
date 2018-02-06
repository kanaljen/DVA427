import numpy as np
import TSM

infile = open('berlin52.tsp', 'r')

# Read instance header
Name = infile.readline().strip().split()[1] # NAME
FileType = infile.readline().strip().split()[1] # TYPE
Comment = infile.readline().strip().split()[1] # COMMENT
Dimension = infile.readline().strip().split()[1] # DIMENSION
EdgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
infile.readline()

# Read node list
nodelist = []
N = int(Dimension)
for i in range(0, int(Dimension)):
    x,y = infile.readline().strip().split()[1:]
    nodelist.append([float(x), float(y)])

# Close input file
infile.close()
dataset = np.array(nodelist)

TSM = TSM.OverHead(n_cities=52, n_salesmen=10)
TSM.test(dataset)

"""TSM.add_cities(dataset)
TSM.create_salesmen()

print(len(TSM.salesman[0].route))

for i in range(len(TSM.salesman)):
	print(TSM.salesman[i].tot_dist)

TSM.fitness_evaluator()

print(TSM.best_salesmen)"""




