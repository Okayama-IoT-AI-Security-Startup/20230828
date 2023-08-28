# hands リアルタイムに処理をする
# 線描をライブラリで行う（drawing_utils​）
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
drw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("MediaPipe Hands", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
