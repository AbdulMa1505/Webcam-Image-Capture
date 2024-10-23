## Webcam Image Capture
- This project captures an image using the computer's webcam and saves it as test.png using the OpenCV library in Python. The program also displays the captured frame for 1 second before exiting.
## Requirements
- Python 3.x
- OpenCV
## Troubleshooting
- If you encounter issues with the webcam, make sure that the camera is not being used by another application and that it is properly connected.
- If you're using multiple webcams, you might need to change cv2.VideoCapture(0) to cv2.VideoCapture(1) or another index.