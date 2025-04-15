import cv2
import os
from image_stitching import ImageStitching
from image_capture import ImageCapture
from object_detection import ObjectDetection

# capture images
capture = ImageCapture(CAM_INDEX = 0) # change index depending on what port the camera is in

# stitch images
stitching = ImageStitching('frames')

# detect image
detector = ObjectDetection('stitched_image.jpg')