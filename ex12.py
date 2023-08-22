import numpy as np
from PIL import Image, ImageDraw
import time

start = time.perf_counter()

img = Image.open('1.png')
w, h = img.size
nimg = np.array(img)

nimg[int(h/3):int(h/3*2), :] = 255-nimg[int(h/3):int(h/3*2), :]  #この行がポイント
nimg[:int(h/3), int(w/3):int(w/3*2)]=255-nimg[:int(h/3), int(w/3):int(w/3*2)]
nimg[int(h/3*2):, int(w/3):int(w/3*2)]=255-nimg[int(h/3*2):, int(w/3):int(w/3*2)]

img=Image.fromarray(nimg)
draw = ImageDraw.Draw(img)
draw.text((10, h-10), f'{time.perf_counter() - start}')
img.show()
img.save('1b.png')
