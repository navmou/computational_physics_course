import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("random.txt")
plt.hist(d, 100)
