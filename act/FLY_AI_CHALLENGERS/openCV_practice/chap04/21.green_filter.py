import cv2

capture = cv2.VideoCapture(0)   # 0번 카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안 됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)       # 프레임 밝기 초기화

title = "test"
cv2.namedWindow(title)

while True:
    ret, frame = capture.read()           # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break      # 스페이스바 누르면 종료

    blue, green, red = cv2.split(frame) # 컬러 영상 채널 분리
    # (200, 100)죄표에서 100x200 크기의 관심 영역 지정
    
    # 관심 영역에서 녹색 성분읠 50만큼 증가
    cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])

    frame = cv2.merge([blue, green, red]) # 단일 채널 영상 합성

    # 관심 영역 테두리를 두께 3의 빨간 색으로 표시
    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)

    cv2.imshow(title, frame)

capture.release()