import cv2

# Open a connection to the webcam (0 is usually the default camera)
imageCapture = cv2.VideoCapture(0)

if not imageCapture.isOpened():
    print("Error: Could not open webcam.")
else:
    result = True
    while result:
        
        ret, frame = imageCapture.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        
        cv2.imshow('Webcam', frame)
        
        
        cv2.imwrite('test.png', frame)
        print("Image captured...")

       
        result = False
        
       
        cv2.waitKey(1000)  # Wait 1000 ms (1 second) before closing

imageCapture.release()
cv2.destroyAllWindows()
