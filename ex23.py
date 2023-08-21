# hands detect
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
drw = mp.solutions.drawing_utils

def checkanddraw(img):
    img_h, img_w, _ = img.shape
    r = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if r.multi_hand_landmarks:
         for h in r.multi_hand_landmarks:
           drw.draw_landmarks(img, h, mp_hands.HAND_CONNECTIONS)
    return img

img = checkanddraw(cv2.imread("1.jpg"))
cv2.imwrite("10.jpg", img)
