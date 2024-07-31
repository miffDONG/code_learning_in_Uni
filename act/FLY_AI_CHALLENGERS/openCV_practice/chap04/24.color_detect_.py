import cv2
import numpy as np

# 이미지 읽기
title = 'color_detection'
image = cv2.imread('images/color_detect.jpg', cv2.IMREAD_COLOR)

if image is None:
    raise Exception("영상 읽기 실패")

# 이미지를 복사하여 결과를 보여줄 이미지 생성
output_image = image.copy()

# 이미지를 회색조로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 원 검출을 위한 HoughCircles 함수 사용
circles = cv2.HoughCircles(
    gray, 
    cv2.HOUGH_GRADIENT, 
    dp=1.2, 
    minDist=20,
    param1=50, 
    param2=30, 
    minRadius=10, 
    maxRadius=100
)

# 원이 검출되었으면
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    
    for (x, y, r) in circles:
        # 원의 중심과 반지름을 그림
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output_image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        
        # 원의 중심에서 해당 색상 샘플링
        mask = np.zeros(gray.shape, dtype=np.uint8)
        cv2.circle(mask, (x, y), r, 255, -1)
        
        mean_color = cv2.mean(image, mask=mask)
        
        # 색상 판별
        b, g, r = mean_color[:3]
        if r > g and r > b:
            color = 'Red'
        elif g > r and g > b:
            color = 'Green'
        elif b > r and b > g:
            color = 'Blue'
        else:
            color = 'Unknown'
        
        # 색상 텍스트를 원의 중심 근처에 그림
        org = (int(x - r), int(y - r))  # 좌표를 정수형으로 변환
        color_text = f'Color: {color}'  # 색상 텍스트
        cv2.putText(output_image, color_text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# 결과 이미지 출력
cv2.imshow(title, output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
