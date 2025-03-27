from ultralytics import YOLO
import cv2
import numpy as np

class ObjectDetection:
    def __init__(self, image_path):
        # Read the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print("Error: Image could not be loaded.")
            return

        # Apply a GaussianBlur to smooth the image and reduce noise
        blurred = cv2.GaussianBlur(image, (5, 5), 0)

        # Use thresholding to create a binary image (black and white)
        _, thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY_INV)

        # Find contours in the binary image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours around detected specks
        speck_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to color image to draw contours
        for contour in contours:
            if cv2.contourArea(contour) > 15:  # Only detect large enough specks (can adjust the threshold)
                # Draw bounding box around specks
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(speck_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show the detected specks on the image
        cv2.imshow('Detected Particles', speck_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()