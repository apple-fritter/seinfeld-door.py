# seinfeld-door.py
## Work-in-progress.
A motion detection python script to play the infamous Seinfeld™ bass clip.

This Python script uses the `OpenCV` library to capture video from a webcam and perform motion detection using a background subtraction algorithm. If motion is detected in the frame, the script uses the playsound library to play a sound file.

## Here's a breakdown of the different parts of the script:

* `import cv2` imports the `OpenCV` library for capturing and processing video frames.
* `import numpy as np` imports the `NumPy` library for numerical computations on arrays.
* `import playsound` imports the playsound library for playing audio files.
* `seinfeld_sound = "seinfeld.mp3"` sets the file path of the audio file to be played.
* `cap = cv2.VideoCapture(0)` creates a VideoCapture object that captures video from the default webcam.
* `fgbg = cv2.createBackgroundSubtractorMOG2()` creates a background subtractor object that will be used to detect motion in the video.
* `while True` loop runs continuously until the user presses the "q" key.
* `ret, frame = cap.read()` captures a frame from the video.
* `fgmask = fgbg.apply(frame)` applies the background subtractor to the frame to obtain a foreground mask, which highlights areas of the frame that have changed from the background.
* `if np.count_nonzero(fgmask) > 10000` checks if the number of non-zero pixels in the foreground mask is greater than a threshold value of 10000. If so, motion is detected and the audio file is played using `playsound(seinfeld_sound)`.
* `cv2.imshow('frame',fgmask)` displays the video frame with the foreground mask overlay.
* `if cv2.waitKey(1) & 0xFF == ord('q')` waits for a key event and checks if the user has pressed the "q" key. If so, the loop is exited.
* `cap.release()` releases the webcam.
* `cv2.destroyAllWindows()` closes all windows created by OpenCV.

## Uses
* This Python script could be useful for anyone who needs to perform motion detection on live video streams from a webcam, such as part of a simple home security system to detect motion and trigger an alarm or notification.
* People who just like terrible comedy.

## Requirements
To run this script, you will need to have several dependencies installed:
* Python: The script requires Python to be installed on your system. You can download Python from the official Python website (`python.org`).
* OpenCV: The script uses the OpenCV library for capturing and processing video frames. You can install OpenCV using pip, the Python package manager, by running the following command in your terminal or command prompt: `pip install opencv-python`.
* NumPy: The script uses the NumPy library for numerical computations on arrays. You can install NumPy using pip by running the following command: `pip install numpy`.
* playsound: The script uses the playsound library for playing audio files. You can install playsound using pip by running the following command: `pip install playsound`.
* A webcam: The script requires a webcam to capture live video frames.
* The seinfeld mp3.

Once you have installed these dependencies, you should be able to run the script by executing the Python file from the command line using `python seinfeld-door.py` (assuming the script file is named "seinfeld-door.py").

## DISCLAIMER:
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
