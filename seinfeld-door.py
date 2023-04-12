import cv2
import numpy as np
from playsound import playsound

# Load the Seinfeld sound MP3 file
seinfeld_sound = "seinfeld.mp3"

# Create a VideoCapture object to capture video from the webcam
cap = cv2.VideoCapture(0)

# Create a background subtractor object to detect motion
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Capture a frame from the video
    ret, frame = cap.read()

    # Apply the background subtractor to the frame to detect motion
    fgmask = fgbg.apply(frame)

    # Check if there is motion in the frame
    if np.count_nonzero(fgmask) > 10000:
        print("Motion detected!")
        playsound(seinfeld_sound)

    # Display the video with motion detection overlay
    cv2.imshow('frame',fgmask)

    # Exit if the user presses "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
