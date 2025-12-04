import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

# Load image
img = cv2.imread("images/face.jpeg")
orig = img.copy()
h, w = img.shape[:2]

# Get landmarks
with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
    res = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if not res.multi_face_landmarks:
        print("No face found")
        exit()
    lm = res.multi_face_landmarks[0]

# Convert landmarks to pixel coords
landmarks = [(int(p.x*w), int(p.y*h)) for p in lm.landmark]

# Draw all landmark points (NO NUMBERS)
for (x, y) in landmarks:
    cv2.circle(img, (x,y), 2, (0,255,0), -1)

# Mouse callback to print nearest landmark index
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Find nearest landmark
        min_dist = 1e9
        min_idx = -1
        for i, (lx, ly) in enumerate(landmarks):
            dist = (x-lx)**2 + (y-ly)**2
            if dist < min_dist:
                min_dist = dist
                min_idx = i
        
        print("Clicked landmark index:", min_idx)
        
        # Draw highlight circle
        temp = img.copy()
        cv2.circle(temp, landmarks[min_idx], 6, (0,0,255), 2)
        cv2.imshow("Landmarks", temp)

# Setup window
cv2.namedWindow("Landmarks", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Landmarks", 900, 1200)
cv2.setMouseCallback("Landmarks", on_click)

while True:
    cv2.imshow("Landmarks", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
