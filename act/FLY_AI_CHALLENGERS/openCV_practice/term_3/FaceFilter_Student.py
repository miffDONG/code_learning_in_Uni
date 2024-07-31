import cv2
import numpy as np
import urllib.request
import os

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {filename}.")

def preprocessing(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        return None, None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray

def get_rot_angle(centers):
    dy = centers[1][1] - centers[0][1]  # 오른쪽 눈과 왼쪽 눈의 y 좌표 차이
    dx = centers[1][0] - centers[0][0]  # 오른쪽 눈과 왼쪽 눈의 x 좌표 차이
    angle = np.degrees(np.arctan2(dy, dx))  # 수평 방향과 이루는 각도 계산
    print("각도: ", angle)
    angle =  360 -  abs(angle)
    return angle

# Haarcascade 파일 다운로드
download_file("https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml", "haarcascade_frontalface_default.xml")
download_file("https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml", "haarcascade_eye_tree_eyeglasses.xml")
download_file("https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_smile.xml", "haarcascade_smile.xml")

# 정면 얼굴 검출기 불러오기
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 눈 검출기 불러오기
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# 웃음 검출기 불러오기
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# 투명도가 포함된 얼굴 이미지 불러오기
image_path = 'C:/code_learning_in_Uni/act/FLY_AI_CHALLENGERS/openCV_practice/term_3/data/images/example3.jpg'
image, gray = preprocessing(image_path)
if image is None:
    raise Exception("영상 파일 읽기 에러")

# 원본 이미지 복사본 생성
original_image = image.copy()

# 얼굴 검출하기
height, width, _ = image.shape
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)

    face_roi_gray = gray[y:y+h, x:x+w]
    face_roi_color = image[y:y+h, x:x+w]

    # 눈 검출하기
    eyes = eye_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(2, 2))

    # 웃음 검출하기
    smile = smile_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=20, minSize=(25, 25))
    print("웃음 검출: ", smile)

    if len(eyes) >= 2:
        # 가장 큰 두 개의 눈을 선택
        eyes = sorted(eyes, key=lambda e: e[2] * e[3], reverse=True)[:2]
        eye_centers = [(x + ex + ew // 2, y + ey + eh // 2) for (ex, ey, ew, eh) in eyes]
        
        # 눈 좌표를 왼쪽에서 오른쪽 순으로 정렬
        eye_centers = sorted(eye_centers, key=lambda center: center[0])  # x 좌표를 기준으로 정렬하여 왼쪽 눈이 먼저 오도록

        # 두 눈 좌표간 각도 계산
        angle = get_rot_angle(eye_centers)

        # 두 눈 사이 중앙 좌표 계산
        eye_center = ((eye_centers[0][0] + eye_centers[1][0]) // 2, (eye_centers[0][1] + eye_centers[1][1]) // 2)
        

        # 안경 이미지 불러오기
        glasses, glasses_gray = preprocessing('C:/code_learning_in_Uni/act/FLY_AI_CHALLENGERS/openCV_practice/term_3/data/filter/glasses.png')

        # 안경 이미지와 얼굴의 비율을 맞춤
        glasses_h, glasses_w, _ = glasses.shape
        eye_distance = np.linalg.norm(np.array(eye_centers[0]) - np.array(eye_centers[1]))
        ratio = eye_distance / glasses_w * 2.0  # 안경 이미지의 크기를 눈 간 거리로 조정
        new_size = (int(glasses_w * ratio), int(glasses_h * ratio))
        resized_glasses = cv2.resize(glasses, dsize=new_size, interpolation=cv2.INTER_AREA)

        resized_h, resized_w, _ = resized_glasses.shape
        glasses_center = (resized_h // 2, resized_w // 2)

        # 안경 이미지 회전
        rot_mat = cv2.getRotationMatrix2D(glasses_center, angle, 1)
        corr_glasses = cv2.warpAffine(resized_glasses, rot_mat, (resized_w, resized_h), cv2.INTER_CUBIC)

        # 안경 이미지를 반영함
        for y in range(corr_glasses.shape[0]):
            for x in range(corr_glasses.shape[1]):
                # 눈 중앙 위치와 안경 사진의 중앙 위치를 맞추기 위한 좌표 계산
                y2 = eye_center[1] - glasses_center[1] + y
                x2 = eye_center[0] - glasses_center[0] + x
                # 안경 이미지의 크기나 전체 이미지의 얼굴 위치가 구석에 쏠려 있는 경우
                # 반영될 안경 이미지가 전체 이미지의 범위를 벗어날 수 있음
                if 0 <= y2 < height and 0 <= x2 < width:
                    if corr_glasses[y, x, 3] > 0:  # 투명도 채널이 존재하고 투명도가 0보다 큰 경우
                        image[y2, x2, :] = corr_glasses[y, x, :-1]
                        
        # 눈 좌표 표시
        for center in eye_centers:
            cv2.circle(image, center, 3, (255, 0, 0), -1)
    else:
        print("눈 미검출")
    
    

# 원본 이미지와 결과 이미지를 수평으로 스택
stacked_images = np.hstack((original_image, image))

# 스택된 이미지 보여주기
cv2.imshow("Original and Glasses", stacked_images)
cv2.waitKey(0)
cv2.destroyAllWindows()