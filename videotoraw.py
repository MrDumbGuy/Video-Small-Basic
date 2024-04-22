import cv2
import matplotlib.colors
import numpy as np
import matplotlib

f = open("datacol.txt", 'a')

colors = { #light = lowercase, dark = uppercase. Encoded as BGR here because I have no clue how HSL works. 
           #Tip: Don't bother trying to add gray. Everything gets approximated to gray.
        'r': (0, 0, 255),
        'R': (0, 0, 139),
        'y': (0, 255, 255),
        'Y': (0, 139, 139),
        'g': (0, 255, 0),
        'G': (0, 139, 0),
        'b': (255, 0, 0),
        'B': (139, 32, 0),
        'c': (0, 255, 255),
        'C': (0, 139, 255),
        'm': (255, 0, 255),
        'M': (139, 0, 139),
        '0': (0, 0, 0),
        '1': (255, 255, 255),
        '2': (128, 128, 128),
        '3': (169, 169, 169),
        '4': (153, 136, 119),
        '5': (79, 79, 47),
        'o': (0, 165, 255),
        'O': (0, 140, 255),
        'w': (45, 82, 160),
        'W': (19, 69, 139),
        }
    
for c in colors:
    colors[c] = matplotlib.colors.rgb_to_hsv(colors[c]) #HSV is more accurate to human perception than RGB.
    print(colors[c])

def get_color_name(pixel):
    min_dist = float('inf')
    color_name = None
    pixel_hsv = matplotlib.colors.rgb_to_hsv(pixel)
    
    for color, value in colors.items():
        dist = np.linalg.norm(np.array(pixel_hsv) - np.array(value))
        
        if dist < min_dist:
            min_dist = dist
            color_name = color

    return color_name


cap = cv2.VideoCapture('cpmcfs.mp4') #Replace this with your own video!

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