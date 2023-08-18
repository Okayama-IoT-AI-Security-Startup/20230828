import cv2
img = cv2.imread("lena.jpg")
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
facerect = cascade.detectMultiScale(gimg)
for (x, y, w, h) in facerect:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0))
cv2.imwrite("markedlena.jpg", img)
