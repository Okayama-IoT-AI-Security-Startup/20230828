import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

masks=[101,195,330,447,364,175,215,227]

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

  while cap.isOpened():
    success, image = cap.read()
    h, w = image.shape[:2]
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image2)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
         wks=np.array([[int(face_landmarks.landmark[i].x*w), int(face_landmarks.landmark[i].y*h)] for i in masks])
         cv2.fillConvexPoly(image, wks, color=(200, 200, 200))
    cv2.imshow('MediaPipe FaceMesh', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
      break

cap.release()
