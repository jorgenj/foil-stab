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

# define the list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

while(1):
    ret ,frame = cap.read()

    if ret == True:
        # loop over the boundaries
        for (lower, upper) in boundaries:
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")
         
            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(frame, lower, upper)
            output = cv2.bitwise_and(frame, frame, mask = mask)
         
            # show the images
            cv2.imshow("preview", np.hstack([frame, output]))
            cv2.waitKey(1)

cv2.destroyAllWindows()
cap.release()
