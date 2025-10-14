import cv2
import numpy as np

image = cv2.imread("apple_tree.jpg")
if image is None:
    print("ERROR: Image not found!")
    exit()

output = image.copy()
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2
mask = cv2.GaussianBlur(mask, (9, 9), 2)

circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
                           param1=50, param2=30, minRadius=5, maxRadius=50)

count = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    count = len(circles[0, :])
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)

print("Number of apples:", count)
cv2.imshow("Apples Detected", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
