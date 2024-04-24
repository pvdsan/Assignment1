# The checkerboard was kept 38 cm away from the camera. The square size is 25mm

# The checker board pattern is detected with one as padding

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Define the camera matrix and distortion coefficients
camera_matrix = np.array([
    [826.1702, 0, 306.2125],
    [0, 815.7698, 233.2915],
    [0, 0, 1]
], dtype="float32")

dist_coeffs = np.array([0.0778, 0.0654, 0, 0], dtype="float32")  # Simplified to two radial components

# Load your image
image_path = 'Calibration_Images\\Image21.png'  # Adjust this path
image = cv2.imread(image_path)
if image is not None:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for matplotlib

# Define the rotation and translation vectors from calibration data for Image 21
rotation_vector = np.array([-0.1215, -0.1354, -1.5621], dtype="float32")
translation_vector = np.array([-68.5465, 63.0514, 494.3451], dtype="float32")  # Already in millimeters

# Example 3D world point in cm
world_point = np.array([[0, 0, 0]], dtype="float32")

# Project the 3D point to 2D using the camera matrix
projected_point, _ = cv2.projectPoints(world_point, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
projected_point = projected_point.squeeze()

# Display the image and the projected point
if image is not None:
    plt.figure(figsize=(8, 6))
    plt.imshow(image)
    plt.scatter([projected_point[0]], [projected_point[1]], color='red', s=10)  # Mark the projected point
    plt.title('Projected 3D Point on 2D Image')
    plt.axis('off')
    plt.show()
else:
    print("Failed to load the image. Check the file path and try again.")



world_point = np.array([[25, 0, 0]], dtype="float32")

# Project the 3D point to 2D using the camera matrix
projected_point, _ = cv2.projectPoints(world_point, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
projected_point = projected_point.squeeze()

# Display the image and the projected point
if image is not None:
    plt.figure(figsize=(8, 6))
    plt.imshow(image)
    plt.scatter([projected_point[0]], [projected_point[1]], color='red', s=10)  # Mark the projected point
    plt.title('Shift by 1 box upwards')
    plt.axis('off')
    plt.show()
else:
    print("Failed to load the image. Check the file path and try again.")

world_point = np.array([[0, 25, 0]], dtype="float32")

# Project the 3D point to 2D using the camera matrix
projected_point, _ = cv2.projectPoints(world_point, rotation_vector, translation_vector, camera_matrix, dist_coeffs)
projected_point = projected_point.squeeze()

# Display the image and the projected point
if image is not None:
    plt.figure(figsize=(8, 6))
    plt.imshow(image)
    plt.scatter([projected_point[0]], [projected_point[1]], color='red', s=10)  # Mark the projected point
    plt.title('Shifted by 1box to right')
    plt.axis('off')
    plt.show()
else:
    print("Failed to load the image. Check the file path and try again.")
