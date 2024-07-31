import numpy as np
import cv2

def onChangeThickness(value):
    global thickness

    thickness = value

def onChangeRadius(value):
    global radius

    radius = value

def onMouse(event, x, y, flags, param):
    global title

    # 마우스 오른쪽 버튼 클릭 시
    if event == cv2.EVENT_RBUTTONDOWN:
        # 클릭 좌표에서 반지름이 20인 원 그리기
        cv2.circle(img, (x, y), radius, (0, 0, 255), 2) # 두께가 2인 빨간 원
    # 마우스 왼쪽 버튼 클릭 시
    elif event == cv2.EVENT_LBUTTONDOWN:
        # 크기 30x30인 사각형 그리기
        cv2.rectangle(img, (x, y), (x+30, y+30), (255, 0, 0), thickness) # 두께가 2인 파란 사각형

    cv2.imshow(title, img)

thickness = 1
radius = 20

img = np.full((200, 300, 3), 255, np.uint8)
title = 'test'
cv2.imshow(title, img)
cv2.createTrackbar('thickness',title,thickness,10,onChangeThickness)
cv2.createTrackbar('radius',title,radius,50,onChangeRadius)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()