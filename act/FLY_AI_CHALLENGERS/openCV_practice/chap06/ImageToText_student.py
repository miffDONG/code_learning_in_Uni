import cv2
import numpy as np
import pytesseract

# Tesseract OCR의 설치 경로를 설정합니다.
TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe" # 테서렉스 설치 경로

# 이미지 파일 경로와 OpenCV 창 이름을 설정합니다.
imgpath = './images/2-1.jpg'  # 이미지 파일 경로
win_name = "Image To Text"  # OpenCV 창 이름
img = cv2.imread(imgpath)   # 이미지를 읽어옵니다.

points = []  # 마우스 클릭으로 얻은 네 꼭짓점 좌표

# 마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global points, img
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow(win_name, img)
        if len(points) == 4:
            cv2.line(img, points[0], points[1], (255, 0, 0), 2)
            cv2.line(img, points[1], points[2], (255, 0, 0), 2)
            cv2.line(img, points[2], points[3], (255, 0, 0), 2)
            cv2.line(img, points[3], points[0], (255, 0, 0), 2)
            cv2.imshow(win_name, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            ImgProcessing()
            text = GetOCR()
            print(text)

# 이미지 처리 함수
def ImgProcessing():
    global img, points
    # 점들을 np.float32로 변환
    pts1 = np.float32(points)
    # 사각형의 너비와 높이 계산
    width = max(abs(points[1][0] - points[0][0]), abs(points[2][0] - points[3][0]))
    height = max(abs(points[3][1] - points[0][1]), abs(points[2][1] - points[1][1]))
    # 변환할 사각형의 좌표 설정
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    # 원근 변환 행렬 계산
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # 원근 변환 적용
    img = cv2.warpPerspective(img, matrix, (int(width), int(height)))
    # 회색조로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 이진화 처리
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # 이진화된 이미지를 반전
    img = cv2.bitwise_not(binary)

# OCR 함수
def GetOCR():
    # 이미지에 대한 전역 변수 설정
    global img
    # OCR 모델 경로 설정
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    # OCR로 텍스트 추출
    text = pytesseract.image_to_string(img, lang='kor+eng')
    return text

# 이미지 표시 및 마우스 이벤트 등록
cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)  # 입력 대기
cv2.destroyAllWindows()
