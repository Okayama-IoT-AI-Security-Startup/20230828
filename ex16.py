# matplotlib 3D（鞍点）グラフサンプル
# plotのviewer（plt.show）をお楽しみ下さい

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

x = np.linspace(-1, 1, 12)
y = np.linspace(-1, 1, 12)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

ax.plot_surface(X, Y, Z, cmap = "summer")

plt.show()
