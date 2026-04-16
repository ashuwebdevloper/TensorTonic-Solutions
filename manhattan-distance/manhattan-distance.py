import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)

    manhattan_distance = np.sum(np.abs(x-y))
    return float(manhattan_distance)
    pass


# Example Usage:
# x = [1, 2], y = [4, 6]
# |1-4| + |2-6| = 3 + 4 = 7.0