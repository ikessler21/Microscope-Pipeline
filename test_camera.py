import cv2

# Initialize the camera (default index is 0)
CAM_INDEX = 0
vidcap = cv2.VideoCapture(CAM_INDEX)

if not vidcap.isOpened():
    print(f"Error: Could not open video stream with camera index {CAM_INDEX}.")
else:
    # Capture and display the camera feed
    while True:
        success, frame = vidcap.read()
        if not success:
            print("Failed to capture frame.")
            break

        # Display the captured frame
        cv2.imshow("Camera Feed", frame)

        # Break the loop if ESC key is pressed
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    # Release the video capture object and close the window
    vidcap.release()
    cv2.destroyAllWindows()