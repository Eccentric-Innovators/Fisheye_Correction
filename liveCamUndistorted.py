import numpy as np
import cv2
import sys

cam = cv2.VideoCapture(1)
cam.set(3,1280) #1920, 1280, 640
cam.set(4,720) #1080, 720, 480
cv2.namedWindow("test")

img_counter = 0

DIM=(1280, 720)
K=np.array([[1213.202703042268, 0.0, 596.7783523710964], [0.0, 1216.2799457964493, 257.77238817119604], [0.0, 0.0, 1.0]])
D=np.array([[-0.126503993300498], [0.03688655131559319], [0.3498539558136208], [-2.006807518705875]])

def undistort(frame):
	map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
	undistorted_img = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
	return undistorted_img

while True:
    ret, frame = cam.read()
    frame = undistort(frame)
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "./720p_correction/720p_live_undistort/img_720p_live_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()