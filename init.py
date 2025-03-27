import cv2
import os
from image_stitching import ImageStitching
from image_capture import ImageCapture
from object_detection import ObjectDetection

# capture images
#capture = ImageCapture()

# stitch images
#stitching = ImageStitching('frames')

# detect image
detector = ObjectDetection('stitched_image.jpg')