#What is the result of the following code?

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b

print(c)

#Create a numpy array of 10 zeros. and reshape it to (2, 5)

import numpy as np
array=np.zeros(10)
print(array)
array = array.reshape(2,5)
print(array)

#Find Mean, Mode, Median, Standard Deviation of the following data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
import statistics

mean = np.mean(data)

median = np.median(data)


print(f" Median: {median}, Mean: {mean}")

print("Standard Deviation of the data is % s "
                    %(statistics.stdev(data)))


#create a 6x6 numpy array with random values and find the min and max values

values= np.random.random((6,6))
print("values")
print(values) 
valuesmin, valuesmax = values.min(), values.max()
print("Min and Max Values:")
print(valuesmin, valuesmax)

#create a 3D numpy array and reshape it to 2D



#create 1D array from this data

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = np.array(data)
print(x)





