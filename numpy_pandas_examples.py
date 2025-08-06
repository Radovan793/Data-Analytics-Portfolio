import numpy as np
import pandas as pd

"""numpy array"""

arr = np.array([1, 2, 3, "klm"]) 
print(arr)

"""numpy array"""

arr = np.array([[1, 2], [3, 4]]) # a NumPy array with 2 dimensions (a matrix), so the .mean() has an extra twist because of the axis argument.
x = arr.mean(axis=0) # → axis=0 mean down columns.
print(arr) 
print(x) # Output: array([2., 3.])

"""numpy mean()"""

arr = np.array([12, 5.65, 49.65, 2, 35, 64, 98])
average = arr.mean()
summ = arr.sum()
print(average)
print(summ)

"""pandas series"""

arr = pd.Series([10, 20, 30])
average = arr.mean()
print(arr)
print(average)  # Output: 20.0