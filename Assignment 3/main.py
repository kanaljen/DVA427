import numpy as np


x = np.arange(1,52)
x = np.append(x,0)
x = np.insert(x,0,0)
print(x)
for i in range(len(x)):
	print(x[i-1])