import cv2
import os
import numpy as np

class ImageStitching:

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.image_files = os.listdir(self.folder_path)
        self.images = []  # Store valid images here

        # Iterate through the files and read valid images
        for image in self.image_files:
            # Check if the file has a valid image extension
            if image.lower().endswith(('.jpg', '.jpeg', 'png')):  # Case-insensitive check
                image_path = os.path.join(self.folder_path, image)
                image_data = cv2.imread(image_path)
                
                if image_data is not None:
                    self.images.append(image_data)
                else:
                    print(f"Warning: Could not read image {image_path}")

        # Check if enough images were found
        if len(self.images) < 2:
            print("Error: Not enough images to perform stitching.")
        else:
            self.stitch_images()

    def stitch_images(self):
        # Create the stitcher object
        stitcher = cv2.Stitcher_create()

        # Perform the stitching
        status, stitched_image = stitcher.stitch(self.images)

        # Check if stitching was successful
        if status == cv2.Stitcher_OK:
            # Make the background white
            stitched_image_with_white_bg = self.make_background_white(stitched_image)
            
            # Save the image
            cv2.imwrite('stitched_image.jpg', stitched_image_with_white_bg)
            print("Stitching completed successfully. Output saved as 'stitched_image.jpg'.")
        else:
            print("Error during stitching: ", status)

        # Optionally, display the stitched image
        # cv2.imshow("Stitched Image with White Background", stitched_image_with_white_bg)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def make_background_white(self, stitched_image):
        # Convert the stitched image to a mask (where black pixels are masked)
        mask = cv2.inRange(stitched_image, (0, 0, 0), (10, 10, 10))  # Adjust threshold if necessary
        
        # Create an output image with white background
        stitched_image_with_white_bg = stitched_image.copy()
        
        # Set all masked (black) pixels to white (255, 255, 255)
        stitched_image_with_white_bg[mask == 255] = [255, 255, 255]
        
        return stitched_image_with_white_bg
