import cv2
import numpy as np

# Load the image
image = cv2.imread('Image_For_Test.jpg')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of yellow color in HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Create a mask with yellow color
mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over contours to get the coordinates
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    # x, y are the coordinates of the top-left corner of the bounding rectangle
    # w, h are the width and height of the rectangle
    print(f"Yellow object found at: X: {x}, Y: {y}, Width: {w}, Height: {h}")

    # Optional: Draw a rectangle around the yellow object
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Optional: Display the image with detected yellow objects
cv2.imshow('Detected Yellow Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
