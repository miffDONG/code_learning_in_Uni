import cv2
import numpy as np
import random

# 이미지 생성
image = np.full((480, 640, 3), 255, np.uint8)

red, blue, green = (0, 0, 255), (255, 0, 0), (0, 255, 0)

circles = []

def check_overlap(new_circle, existing_circles):
    x, y, r = new_circle
    for ex, ey, er in existing_circles:
        distance = np.sqrt((x - ex)**2 + (y - ey)**2)
        if distance < (r + er):
            return True
    return False

for i in range(5):
    attempts = 0
    while attempts < 100:  # 최대 100번 시도
        x = np.random.randint(100, 500)
        y = np.random.randint(80, 400)
        radius = np.random.randint(10, 50)
        
        if not check_overlap((x, y, radius), circles):
            center = (x, y)
            color = random.choice([red, blue, green])
            cv2.circle(image, center, radius, color, -1)
            circles.append((x, y, radius))
            break
        
        attempts += 1
    
    if attempts == 100:
        print(f"원 {i+1}을 그리는 데 실패했습니다.")

# 원 찾기 및 사각형 그리기 (이전 코드와 동일)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 윤곽 찾기 -> 리스트 

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    
    # 원의 색상 확인
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)
    color = cv2.mean(image, mask=mask)[:3]
    
    # 색상에 따라 사각형 그리기
    if color[2] > color[0] and color[2] > color[1]:  # 빨간색
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(image, 'Red', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    elif color[0] > color[1] and color[0] > color[2]:  # 파란색
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, 'Blue', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    else:  # 녹색
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, 'Green', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

# 결과 표시
cv2.imshow('Circles with Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()