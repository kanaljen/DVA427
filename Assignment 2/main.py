import classifier
import numpy as np

# Load dataset from file
#dataset = np.loadtxt('iris_data.dat', delimiter=',', dtype={'names':('x1','x2','x3','x4','species'),'formats':('f','f','f','f','S15')})

dataset = np.loadtxt('iris_data.dat', delimiter=' ',usecols=(0,1,2,3), unpack=True)
f_name = np.loadtxt('iris_data.dat', delimiter=' ',usecols=(4), dtype = int, unpack=True)
print(len(dataset[:,0]))
print(len(dataset[0,:]))
print(f_name[52])
#print(type(x1[0]))
#print(x1.shape)
#print(x1[0].shape)
#print(x2.shape)
#print(x3.shape)
#print(x4.shape)
#print(f_name.shape)
#print(dataset.shape)   	
#tset = np.array([dataset])
#print(type(tset[0][0]))
#print(x1)
#x1_min = np.amin(x1)
#x1_max = np.amax(x1)
#print(x1_min)
#print(x1_max)

fuzzy = classifier.Fuzzy_classifier(amount_of_flowers=150)
a = fuzzy.test(dataset)

right_answer = 0
for i in range(len(dataset[0,:])):
#for i in range(100,150):
	print(fuzzy.iris[i].species)
	if fuzzy.iris[i].species == f_name[i]:
		right_answer = right_answer + 1
print(type(fuzzy.iris[i].species))
print(type(f_name[i]))
print('answer is = %d',right_answer)
print('Accuracy of',right_answer/150,'%')
