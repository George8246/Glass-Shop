#face_mask.py
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import cv2
import dlib

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks/shape_predictor_68_face_landmarks.dat")

print("[INFO] camera sensor warming up...")
vs = VideoStream(0, framerate = 30).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
    # grayscale
    frame = vs.read()
    frame = imutils.resize(frame, height=550)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     # detect faces in the grayayscale frame
    rects = detector(gray, 0)

    # loopop over found faces
    for rect in rects:
        shape = predictor(frame, rect)
        shape = face_utils.shape_to_np(shape)

        for (i, (x, y)) in enumerate(shape):
            # face features number
            print(i)
            print(x)
            print(y)
     
    key = cv2.waitKey(1) & 0xFF
     # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # show the frame
    cv2.imshow("Face Mask", frame)

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

#face_mask.py
...
...
# loop over the frames from the video stream
while True:
        for (i, (x, y)) in enumerate(shape):
            if (i + 1) == 37:
                eyeLeftSide = x - 40
            if (i + 1) == 38:
                eyeTopSide = y - 30
            if (i + 1) == 46:
                eyeRightSide = x + 40
            if (i + 1) == 48:
                eyeBottomSide = y + 30

        eyesWidth= eyeRightSide - eyeLeftSide
        if eyesWidth < 0:
            eyesWidth = eyesWidth * -1
        # add glasses
        fitedGlass = imutils.resize(glass, width=eyesWidth)

...
...

#face_mask.py
...
import dlib
from watermarking import watermarking
...
...
# load glasses
glasses = cv2.imread("images/1.png", cv2.IMREAD_UNCHANGED)

# loop over the frames from the video stream
while True:
    ...
    ...
    for rect in rects:
       fitedGlass = imutils.resize(glass, width=eyesWidth)
       frame = watermarking(frame, fitedGlass, x= eyeLeftSide, y= eyeTopSide)
       
    cv2.imshow("Face Mask", frame)
   
