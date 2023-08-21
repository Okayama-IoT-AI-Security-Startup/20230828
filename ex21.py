# open-cvがインストールされているかは，import vc2 でチェックしてみてください．
# python -c "import cv2"
# で，エラーが戻らないことを確認します．
# "lena.jpg" は https://github.com/opencv/opencv/raw/4.x/samples/data/lena.jpg
#  "haarcascade_frontalface_alt.xml" は https://github.com/opencv/opencv/raw/4.x/data/haarcascades/haarcascade_frontalface_alt.xml
# もしくは，cv2.data.haacascades に記述されています（python -c "import cv2; print(cv2.data.haarcascades)"）

import cv2
img = cv2.imread("lena.jpg")
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
facerect = cascade.detectMultiScale(gimg)
for (x, y, w, h) in facerect:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0))
cv2.imwrite("markedlena.jpg", img)
