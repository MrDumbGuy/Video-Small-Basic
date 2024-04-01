import cv2
import numpy as np

f = open("data.txt", 'a')

def get_color_name(pixel):
    colors = {
        'r': (0, 0, 255),
        'R': (0, 0, 139),
        'y': (0, 255, 255),
        'Y': (0, 139, 139),
        'g': (0, 255, 0),
        'G': (0, 139, 0),
        'b': (255, 0, 0),
        'B': (139, 0, 0),
        'c': (0, 255, 255),
        'C': (0, 139, 139),
        'm': (255, 0, 255),
        'M': (139, 0, 139),
        '0': (0, 0, 0),
        '1': (255, 255, 255),
    }

    min_dist = float('inf')
    color_name = None

    for color, value in colors.items():
        dist = np.linalg.norm(np.array(pixel) - np.array(value))
        if dist < min_dist:
            min_dist = dist
            color_name = color

    return color_name

cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            color = get_color_name(frame[i, j])
            f.write(color)

cap.release()
cv2.destroyAllWindows()
