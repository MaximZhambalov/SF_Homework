import numpy as np

def shuffle_seed(a):
    s = np.random.randint(0, 2**32 - 1)
    np.random.seed (s)
    b = np.random.shuffle(a)
    return (b, s)