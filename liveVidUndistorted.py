import numpy as np
import cv2
import time

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('undistorted_720p.avi',fourcc, 20.0, (1280,720))

DIM=(1280, 720)
K=np.array([[1213.202703042268, 0.0, 596.7783523710964], [0.0, 1216.2799457964493, 257.77238817119604], [0.0, 0.0, 1.0]])
D=np.array([[-0.126503993300498], [0.03688655131559319], [0.3498539558136208], [-2.006807518705875]])

start_time = time.perf_counter()
while(cap.isOpened()):
    ret, frame = cap.read()
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    frame = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    #print(frame.shape)
    if ret==True:
        # frame = cv2.flip(frame,1)
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

end_time = time.perf_counter()
run_time = end_time - start_time
print("Total video time = {} secs".format(round(run_time, 3)))

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()