# import cv2
# import numpy as np
import subprocess
#
# # Load the image
# image_path = r'C:\Users\yogev\Desktop\Lital_Rafi_Project\Color_Y.png'
# # image_path = r'C:\Users\yogev\Downloads\TEST_Y.jpg'
# image = cv2.imread(image_path)
#
# # Check if the image is loaded correctly
# if image is None:
#     print("Error: Image not found or the path is incorrect.")
#     exit()
#
# # Convert the image to HSV color space
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
# # Define the range of yellow color in HSV
# lower_yellow = np.array([20, 100, 100])
# upper_yellow = np.array([30, 255, 255])
#
# # Create a mask with yellow color
# mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
#
# # Find contours in the mask
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# X_CA = [] # Center Of AREA of EACH yellow color X
# Y_CA = [] # Center Of AREA of EACH yellow color Y
# # Iterate over contours to get the coordinates
# for cnt in contours:
#     # Get bounding rectangle for each contour
#     x, y, w, h = cv2.boundingRect(cnt)
#     # Draw a rectangle around the yellow object
#     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#     # Calculate the center of the area using moments
#     M = cv2.moments(cnt)
#     if M["m00"] != 0:
#         cX = int(M["m10"] / M["m00"])
#         cY = int(M["m01"] / M["m00"])
#     else:
#         # Approximate the center for very thin contours
#         cX, cY = x + w // 2, y + h // 2
#
#     print(f"Yellow object found at: Center X: {cX}, Center Y: {cY}")
#
#     # Draw a red circle at the center
#     cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
#     X_CA.append(cX)
#     Y_CA.append(cY)
#
# # Optional: Display the image with detected yellow objects and their centers
# cv2.imshow('Detected Yellow Objects', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Optional: Save the image
# path = r'C:\Users\yogev\Desktop\Lital_Rafi_Project\Image_For_Test.jpg'
# cv2.imwrite(path, image)
# # Convert vectors to comma-separated strings
# vector1_str = ','.join(map(str, X_CA))
# vector2_str = ','.join(map(str, Y_CA))
# # Define the command to call MATLAB executable
# exe_file_matlab = r'C:\Users\yogev\Desktop\Lital_Rafi_Project\CarPP\for_testing\CarPP.exe'
# command = [exe_file_matlab, path, vector1_str, vector2_str]
#
# # Run the command
# subprocess.run(command)


import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_and_get_centers(image_path, path_to_save):
    # Load the image from the specified path
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the range for yellow color
    yellow_lower = np.array([22, 120, 120], dtype="uint8")
    yellow_upper = np.array([30, 255, 255], dtype="uint8")

    # Convert to HSV and create a mask
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image_hsv, yellow_lower, yellow_upper)

    # Apply noise reduction
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours and sort them
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    centers = []

    # Draw rectangles and find centers
    for contour in sorted_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)
        center = (x + w // 2, y + h // 2)
        cv2.circle(image_rgb, center, 5, (0, 0, 255), -1)
        centers.append(center)

    # Display the image
    plt.figure(figsize=(8, 8))
    plt.imshow(image_rgb)
    plt.title('Detected Tennis Balls with Centers')
    plt.axis('off')

    plt.show()
    cv2.imwrite(path_to_save, image)
    return centers

def extract_xy(centers):
    x_values = [center[0] for center in centers]
    y_values = [center[1] for center in centers]
    return x_values, y_values

# Replace with your local image path
#image_path = r'C:\Users\yogev\Desktop\Lital_Rafi_Project\Color_Y2.png'
image_path = r'C:\Users\rafi1\final_project\Collecting-balls-robot-algorithm-main\Collecting-balls-robot-algorithm-main\Color_Y2.png'
#path_to_save = r'C:\Users\yogev\Desktop\Lital_Rafi_Project\Image_For_Test.jpg'
path_to_save = r'C:\Users\rafi1\final_project\Collecting-balls-robot-algorithm-main\Collecting-balls-robot-algorithm-main\Image_For_Test.jpg'
centers = draw_and_get_centers(image_path, path_to_save)

# Extract x and y values
x_values, y_values = extract_xy(centers)
print("X values:", x_values)
print("Y values:", y_values)
# cv2.imshow('Detected Yellow Objects', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Optional: Save the image

# Convert vectors to comma-separated strings
vector1_str = ','.join(map(str, x_values))
vector2_str = ','.join(map(str, y_values))
# Define the command to call MATLAB executable
#exe_file_matlab = r'C:\Users\yogev\Desktop\Lital_Rafi_Project\CarPP\for_testing\CarPP.exe'
exe_file_matlab = r'C:\Users\rafi1\final_project\Collecting-balls-robot-algorithm-main\Collecting-balls-robot-algorithm-main\CarPP\for_Testing\CarPP.exe'
command = [exe_file_matlab, path_to_save, vector1_str, vector2_str]

# Run the command
subprocess.run(command)
