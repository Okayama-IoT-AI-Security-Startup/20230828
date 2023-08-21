# OpenCV 画像の加算，下の例は置き換え
h, w = fore_img.shape[:2]
back_img[dy:dy+h, dx:dx+w] = fore_img

# 矩形変換は
p_original = np.float32([[0,0], [473,55], [14, 514], [467, 449]])
p_trans = np.float32([[0,0], [524,0], [0,478], [524,478]])
 
M = cv2.getPerspectiveTransform(p_original, p_trans)
i_trans = cv2.warpPerspective(i, M, (524, 478))
