import numpy as np, cv2

image = cv2.imread('./act/FLY_AI_CHALLENGERS/openCV_practice/chap08/images/perspective.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일을 읽기 에러")

pts1 = np.float32([(80,40),(315,133),(75,300),(335,300)])
pts2 = np.float32([(50,60),(340,60),(50,320),(340,320)])

perspect_mat = cv2.getPerspectiveTransform(pts1,pts2)


dst = cv2.warpPerspective(image,perspect_mat,image.shape[1::-1],cv2.INTER_CUBIC)

cv2.imshow("image", image)
cv2.imshow("dst_perspective", dst)
cv2.waitKey(0)