from PIL import Image, ImageDraw
import time
img = Image.open('1.png')
w, h = img.size

for x in range(w):
        for y in range(h):
                if (x > w/3 and x < w/3*2) or (y > h/3 and y < h/3*2):
                        r,g,b = img.getpixel((x,y))
                        img.putpixel((x,y),(255-r,255-g,255-b))

img.show()
draw = ImageDraw.Draw(img)
draw.text((10, h-10), f'{time.perf_counter() - start}')
img.save('1a.png')
