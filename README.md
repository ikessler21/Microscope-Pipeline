# Microplastic Detection in Soil Samples

This is an open-source project for detecting microplastics in soil samples using a Dino-Lite camera microscope and a 3D printer. The project integrates the **DNX-Python-API** for camera control, which is available on GitHub.

## DISCLAIMER

To use this application in tandem with the Dino-Lite camera microscope, you need access to the **DNX-Python-API**. This API is available on GitHub. To make it work, you must contact the manufacturers directly to gain access to files that are not publicly available. According to their README, you need the following files:

- `DNX64.dll`
- `DNX32.dll`
- `libusbK.dll`

These files should be placed in the same directory after installing **DNX64**. For access to **DNX64**, please contact your [local distributor](https://www.dino-lite.com/contact01.php). For further details on the process, refer to the Dino-Lite README and their website.

## Setup Instructions

### 1. Camera Setup

Once the DNX API is set up and the camera is connected to your computer, you need to verify that the camera index is correct. 

- Run the `test_camera.py` file to test the camera feed.
- **Important**: Use the **ESCAPE** key to exit the window.
- If the feed displayed is from the desired microscope camera, no further changes are needed.
- If the feed is incorrect, change the `CAM_INDEX` in the `test_camera.py` file (set it to `1`, `2`, etc.) and rerun the script until you find the correct port index. The correct index may vary depending on the computer.

### 2. Using the 3D Printer

If you're using a 3D printer to automate the process, use the provided **G-Code** as a path for your printer to follow. Each G-Code comes with custom timing settings for photo capture, as the path timing and number of stops may vary based on the field of view.

- Select the corresponding G-Code based on your settings.
- The program will take photos at various points along the path based on the timing settings in the G-Code.

### 3. Running the Program

After the camera is set up and the 3D printer is ready (if applicable), run the `init.py` script.

- You will be prompted in the terminal with: **"Press Enter to Continue"**.
- Press Enter when the camera reaches the first stop in its path.
- The program will proceed automatically from there.

### 4. Program Runtime

The runtime of the program depends on the area size you select. Typical runtimes are:

- Smallest area: **5 minutes**
- Largest area: **Up to 2 hours**

### 5. Results

Once the program completes, a window will display the detected particles in bounding boxes, along with additional information for analysis.

## Conclusion

This project provides a streamlined method to detect microplastics in soil samples. After setting up the camera and running the program, you can analyze the results for microplastic detection. If you encounter any issues with the camera setup or running the program, refer to the **DNX-Python-API** documentation and the Dino-Lite resources for further assistance.
