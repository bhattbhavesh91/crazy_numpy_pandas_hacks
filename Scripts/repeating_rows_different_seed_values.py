import numpy as np
import pandas as pd


x = np.arange(10)
x = np.tile(x, (5, 1))
print(x)

y = np.apply_along_axis(np.random.permutation, 1, x)
print(y)
