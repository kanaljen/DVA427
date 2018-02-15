import classifier
import numpy as np


dataset = np.loadtxt('iris_data.dat', delimiter=' ',
                     usecols=(0, 1, 2, 3), unpack=True)
f_name = np.loadtxt('iris_data.dat', delimiter=' ',
                    usecols=(4), dtype=int, unpack=True)


fuzzy = classifier.Fuzzy_classifier(amount_of_flowers=150)
fuzzy.test(dataset)

right_answer = 0
for i in range(len(dataset[0, :])):

    if fuzzy.iris[i].species == f_name[i]:
        right_answer += 1

print('Answer is =', right_answer)
print('Accuracy of', right_answer / 150 * 100, '%')
