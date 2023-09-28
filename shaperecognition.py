import numpy as np
import cv2 as cv


stream = cv.VideoCapture(0)
if not stream.isOpened():
    print("Camera failed to open")
    exit()

RED_LOWTRESH = np.array([0, 145, 145])
RED_HIGHTRESH = np.array([10, 240, 240])


# Setup SimpleBlobDetector parameters.
params = cv.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 200
params.maxThreshold = 255
# Filter by Area.
params.filterByArea = True
params.minArea = 1000
params.maxArea = 100000
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.5
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.1
detector = cv.SimpleBlobDetector_create(params)

while(True):

    ret, frame = stream.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
         # Our operations on the frame come here
    HSVframe = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    HSVframe = cv.blur(HSVframe, (3, 3))
    colorMask = cv.inRange(HSVframe, RED_LOWTRESH, RED_HIGHTRESH)
    colorMaskInverted = cv.bitwise_not(colorMask)
    colorOutput = cv.bitwise_and(frame, frame, mask=colorMask)
    gray = cv.cvtColor(colorOutput, cv.COLOR_BGR2GRAY)

    keypoints = detector.detect(colorMaskInverted)
    frame = cv.drawKeypoints(frame, keypoints, np.array([]), (0,255,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # cv.imshow('frame',  frame)
    cv.imshow("output", np.hstack([frame, colorOutput]))
    if cv.waitKey(1) == ord('q'):
        break
    # When everything done, release the capture
stream.release()
cv.destroyAllWindows()
