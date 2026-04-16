import numpy as np

def sigmoid(x):
    # Converting x to a numpy array ensures the "-" operator works element-wise
    x = np.asarray(x) 
    return 1 / (1 + np.exp(-x))

# Now this will work perfectly!
x = [0, 2, -2]
print(sigmoid(x))