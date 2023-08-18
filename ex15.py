import matplotlib.pyplot as plt 
from PIL import Image
import numpy as np
img = np.array(Image.open("lena.jpg").convert("L"))
fig, ax = plt.subplots()
ax.imshow(img, cmap="gray")
plt.show()
