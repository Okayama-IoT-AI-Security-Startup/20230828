import cv2​
import mediapipe as mp​

mp_drawing = mp.solutions.drawing_utils​
mp_face_mesh = mp.solutions.face_mesh​

cap = cv2.VideoCapture(0)​

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:​

  while cap.isOpened():​
    success, image = cap.read()​
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)​
    results = face_mesh.process(image2)​
    if results.multi_face_landmarks:​
      for face_landmarks in results.multi_face_landmarks:​
        mp_drawing.draw_landmarks(image, face_landmarks)​
    cv2.imshow('MediaPipe FaceMesh', image)​
    if cv2.waitKey(5) & 0xFF == ord('q'):​
      break​

cap.release()​
