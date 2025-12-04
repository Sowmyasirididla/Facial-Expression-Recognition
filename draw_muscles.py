import cv2
import numpy as np

def mean_point(landmarks, indices):
    pts = np.array([landmarks[i] for i in indices])
    return tuple(np.mean(pts, axis=0).astype(int))

def draw_band(img, p1, p2, color=(0,0,255), thickness=20):
    overlay = img.copy()
    cv2.line(overlay, p1, p2, color, thickness)
    cv2.circle(overlay, p1, thickness//2, color, -1)
    cv2.circle(overlay, p2, thickness//2, color, -1)
    cv2.addWeighted(overlay, 0.45, img, 0.55, 0, img)

def draw_muscles(img, landmarks, muscle_dict):
    output = img.copy()
    for name, data in muscle_dict.items():
        origin_center = mean_point(landmarks, data["origin"])
        insertion_center = mean_point(landmarks, data["insertion"])
        draw_band(output, origin_center, insertion_center, data["color"], 18)
    return output
