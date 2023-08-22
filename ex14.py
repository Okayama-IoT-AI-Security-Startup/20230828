import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5,6,7]
y = [4,54,3,2,34,53,9]
fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig("graph.png")
