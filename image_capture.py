import cv2
import os
import numpy as np

class ImageCapture:

    def __init__(self):
        self.folder_path = 'frames'
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        CAM_INDEX = 0  # Assuming webcam index is 0, change if necessary
        self.vidcap = cv2.VideoCapture(CAM_INDEX)

        if not self.vidcap.isOpened():
            print("Error: Could not open video stream.")
            return
        
        self.frame_width = int(self.vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        self.count = 0
        self.capture_images()

    def laplacian_variance(self, image):
        """Calculate the Laplacian variance of the image for sharpness assessment"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Laplacian(gray, cv2.CV_64F).var()

    def capture_images(self):
        """Capture images at intervals, assess focus, and select best one."""
        input("Press Enter to continue...")
        while self.count < 10:
            best_focus = 0
            best_image = None
            frames = []

            print(f"Capturing set {self.count + 1}...")

            # Capture multiple frames for each interval
            for i in range(5):  # Capture 5 frames for each set
                
                key = cv2.waitKey(150)
                
                success, image = self.vidcap.read()
                if not success:
                    print("Failed to capture frame.")
                    break

                frames.append(image)
                focus_value = self.laplacian_variance(image)
                print(f"Focus of frame {i+1}: {focus_value}")

                if focus_value > best_focus:
                    best_focus = focus_value
                    best_image = image

            # Save the best image based on focus
            if best_image is not None:
                frame_filename = os.path.join(self.folder_path, f"frame{self.count}.jpg")
                cv2.imwrite(frame_filename, best_image)
                print(f"Saved frame {self.count} with best focus.")

            self.count += 1
            key = cv2.waitKey(100)

    def __del__(self):
        """Release the video capture when done."""
        if self.vidcap.isOpened():
            self.vidcap.release()

if __name__ == "__main__":
    capture = ImageCapture()