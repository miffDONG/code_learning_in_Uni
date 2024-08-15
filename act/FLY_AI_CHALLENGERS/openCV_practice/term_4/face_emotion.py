import cv2
import mediapipe as mp
import pyautogui
import math

# MediaPipe 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# 비디오 캡처 시작
cap = cv2.VideoCapture(0)

def calculate_distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지 전처리
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 엄지와 검지 끝 점 추출
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # 엄지와 검지 사이의 거리 계산
            thumb_index_distance = calculate_distance(thumb_tip, index_tip)

            # 핀치 감지 기준
            pinch_threshold = 0.05

            if thumb_index_distance < pinch_threshold:
                pyautogui.press('space')             
                print("Space bar pressed")

    # 결과를 화면에 표시
    cv2.imshow('Hand Tracking', frame)

    # 'q'를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
