import cv2
import mediapipe as mp

# File where muscles will be saved
MUSCLE_FILE = "muscles.py"

# Image
IMAGE_PATH = "images/face.jpeg"

# MUSCLE GROUPS YOU WILL FILL
muscle_points = {
    "frontalis_origin": [],
    "frontalis_insertion": [],
    "orbicularis_oculi": [],
    "zygomaticus_origin": [],
    "zygomaticus_insertion": []
}

current_muscle = None

# -------------------------------------
# Save to muscles.py automatically
# -------------------------------------
def save_to_file():
    with open(MUSCLE_FILE, "w") as f:
        f.write("MUSCLES = {\n")
        for muscle, indices in muscle_points.items():
            f.write(f"    '{muscle}': {indices},\n")
        f.write("}\n")
    print("\n>>> muscles.py updated successfully!\n")

# -------------------------------------
# Load image
# -------------------------------------
img = cv2.imread(IMAGE_PATH)
if img is None:
    print("ERROR: Could not load image.")
    exit()
orig = img.copy()
h, w = img.shape[:2]

# -------------------------------------
# Get landmarks using MediaPipe
# -------------------------------------
mp_face_mesh = mp.solutions.face_mesh

with mp_face_mesh.FaceMesh(static_image_mode=True) as fm:
    res = fm.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if not res.multi_face_landmarks:
        print("Error: No face detected.")
        exit()

landmarks = [(int(p.x*w), int(p.y*h)) for p in res.multi_face_landmarks[0].landmark]

# Draw green landmark dots
for (x, y) in landmarks:
    cv2.circle(img, (x, y), 2, (0,255,0), -1)

# -------------------------------------
# Find nearest landmark to click
# -------------------------------------
def nearest_landmark(x, y):
    best = -1
    best_dist = 10**9
    for i, (lx, ly) in enumerate(landmarks):
        d = (lx-x)**2 + (ly-y)**2
        if d < best_dist:
            best_dist = d
            best = i
    return best

# -------------------------------------
# Mouse click event
# -------------------------------------
def mouse_click(event, x, y, flags, param):
    global current_muscle, img

    if event == cv2.EVENT_LBUTTONDOWN:
        if current_muscle is None:
            print(">>> ERROR: Select a muscle first (press keys 1–5)")
            return

        idx = nearest_landmark(x, y)
        muscle_points[current_muscle].append(idx)

        print(f"Added index {idx} → {current_muscle}")

        # Draw highlight
        img = orig.copy()
        for m_group, pts in muscle_points.items():
            for p in pts:
                cv2.circle(img, landmarks[p], 6, (0,0,255), 2)
        for (lx, ly) in landmarks:
            cv2.circle(img, (lx, ly), 2, (0,255,0), -1)

        cv2.imshow("Image", img)
        save_to_file()

# -------------------------------------
# Window setup
# -------------------------------------
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 900, 1200)
cv2.setMouseCallback("Image", mouse_click)

print("\n======================")
print("   KEYBOARD CONTROLS")
print("======================")
print("1 = frontalis_origin")
print("2 = frontalis_insertion")
print("3 = orbicularis_oculi")
print("4 = zygomaticus_origin")
print("5 = zygomaticus_insertion")
print("----------------------")
print("U = Undo last point")
print("C = Clear current muscle")
print("R = Reset all muscles")
print("Q = Quit")
print("======================\n")

# -------------------------------------
# Main Loop
# -------------------------------------
while True:
    cv2.imshow("Image", img)
    key = cv2.waitKeyEx(20)

    if key in [ord('q'), ord('Q')]:
        print("\nExiting...")
        break

    elif key == ord('1'):
        current_muscle = "frontalis_origin"
        print("\n>>> Selected: frontalis_origin")

    elif key == ord('2'):
        current_muscle = "frontalis_insertion"
        print("\n>>> Selected: frontalis_insertion")

    elif key == ord('3'):
        current_muscle = "orbicularis_oculi"
        print("\n>>> Selected: orbicularis_oculi")

    elif key == ord('4'):
        current_muscle = "zygomaticus_origin"
        print("\n>>> Selected: zygomaticus_origin")

    elif key == ord('5'):
        current_muscle = "zygomaticus_insertion"
        print("\n>>> Selected: zygomaticus_insertion")

    # -----------------------------
    # UNDO (U)
    # -----------------------------
    elif key in [ord('u'), ord('U')]:
        if current_muscle and len(muscle_points[current_muscle]) > 0:
            removed = muscle_points[current_muscle].pop()
            print(f">>> UNDO: removed {removed} from {current_muscle}")
            save_to_file()
            img = orig.copy()
            for m_group, pts in muscle_points.items():
                for p in pts:
                    cv2.circle(img, landmarks[p], 6, (0,0,255), 2)

    # -----------------------------
    # CLEAR CURRENT MUSCLE (C)
    # -----------------------------
    elif key in [ord('c'), ord('C')]:
        if current_muscle:
            muscle_points[current_muscle] = []
            print(f">>> CLEARED: {current_muscle}")
            save_to_file()
            img = orig.copy()
            for m_group, pts in muscle_points.items():
                for p in pts:
                    cv2.circle(img, landmarks[p], 6, (0,0,255), 2)

    # -----------------------------
    # RESET ALL (R)
    # -----------------------------
    elif key in [ord('r'), ord('R')]:
        for k in muscle_points:
            muscle_points[k] = []
        print(">>> RESET: All muscle points cleared.")
        save_to_file()
        img = orig.copy()

cv2.destroyAllWindows()
