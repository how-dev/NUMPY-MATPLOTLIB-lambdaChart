import math
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-math.pi, math.pi, 1000)

x = np.cos(31.4159265358979 * t - 5.75958653158129)
y = np.cos(47.1238898038469 * t)

plt.plot(x, y)

plt.ylim(-2, 2)
plt.grid()
plt.show()
