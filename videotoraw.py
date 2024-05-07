import cv2
import matplotlib.colors
import matplotlib

f = open("test.txt", 'a')

colors = {
    '0': (0, 0, 0),
    '1': (31, 31, 31),
    '2': (63, 63, 63),
    '3': (95, 95, 95),
    '4': (127, 127, 127),
    '5': (159, 159, 159),
    '6': (191, 191, 191),
    '7': (255, 255, 255),
}
    
for c in colors:
    colors[c] = sum(colors[c])/len(colors[c])
    print(colors[c])

def get_color_name(pixel):
    pixel = sum(pixel)/len(pixel)
    min_dist = float('inf')
    color_name = None
    
    for color, value in colors.items():
        dist = abs(value - pixel)
        
        if dist < min_dist:
            min_dist = dist
            color_name = color

    return color_name


cap = cv2.VideoCapture('input.mp4') #Replace this with your own video!

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