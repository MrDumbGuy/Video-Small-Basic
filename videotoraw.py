import cv2
import matplotlib.colors
import matplotlib

f = open("output.txt", 'a')

colors = {
    '0': 0,
    '1': 32,
    '2': 64,
    '3': 96,
    '4': 128,
    '5': 160,
    '6': 192,
    '7': 234,
    '8': 255,
}
    
for c in colors:
    print(colors[c])

def get_color_name(pixel):
    pixel = sum(pixel)/len(pixel)
    min_dist = float('inf')
    final_color_name = None
    
    for color, value in colors.items():
        dist = abs(value - pixel)
        
        if dist < min_dist:
            min_dist = dist
            final_color_name = color

    return final_color_name


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
