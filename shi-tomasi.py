import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
	help="path to input video file")
args = vars(ap.parse_args())

print("[INFO] Video : {}".format(args['video']))
cap = cv2.VideoCapture(args['video'])

cv2.startWindowThread()
cv2.namedWindow("preview")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(1):
    ret ,frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
        corners = np.int0(corners)
        for i in corners:
            x,y = i.ravel()
            cv2.circle(frame,(x,y),3,255,-1)


        cv2.imshow('preview', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break

cv2.destroyAllWindows()
cap.release()
