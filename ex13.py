import numpy as np
from PIL import Image, ImageDraw
import time

start = time.perf_counter()

img = Image.open('1.png')
w, h = img.size
nimg = np.array(img)

nmask=np.array([[(x>w/3 and x < w/3*2) or (y>h/3 and y<h/3*2) for x in range(w)] for y in range(h)])
nimg[nmask]=255-nimg[nmask]

img=Image.fromarray(nimg)
draw = ImageDraw.Draw(img)
draw.text((10, h-10), f'{time.perf_counter() - start}')
img.show()
img.save('1c.png')
