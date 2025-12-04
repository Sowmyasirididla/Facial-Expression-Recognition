import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

def get_landmarks(image):
    h, w = image.shape[:2]
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return None
        
        lm_xy = []
        for lm in result.multi_face_landmarks[0].landmark:
            lm_xy.append((int(lm.x * w), int(lm.y * h)))
        return lm_xy
