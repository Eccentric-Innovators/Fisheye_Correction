import numpy as np
import cv2
import config

def captureVid(src, dest, quality):
    cap = cv2.VideoCapture(src)
    cap.set(3,config.qualities[quality][0])
    cap.set(4,config.qualities[quality][1])
    cv2.namedWindow("Camera")
    start = False

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (config.qualities[quality][0],config.qualities[quality][1]))

    while(cap.isOpened()):
        ret, frame = cap.read()
        #print(frame.shape)
        if ret==True:
            # frame = cv2.flip(frame,1)
            if start == True:
                out.write(frame)

            cv2.imshow('Camera',frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                break

            if k%256 == 32:
                start = not start
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()