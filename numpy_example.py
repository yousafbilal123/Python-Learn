#import numpy as np

#arr = np.array([1, 2, 3, 4, 5])

#print(arr)

#print(type(arr))
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()