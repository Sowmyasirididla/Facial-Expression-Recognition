import cv2
from get_landmarks import get_landmarks
from draw_muscles import draw_muscles
from muscles import MUSCLES

img = cv2.imread("images/face.jpg")
landmarks = get_landmarks(img)

if landmarks is None:
    print("No face found")
    exit()

out = draw_muscles(img, landmarks, MUSCLES)

cv2.imshow("Muscle Overlay", out)
cv2.imwrite("output.jpg", out)
cv2.waitKey(0)
