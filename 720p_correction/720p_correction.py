import numpy as np
import cv2
import sys
import time

# You should replace these 3 lines with the output in calibration step
DIM=(1280, 720)
K=np.array([[1213.202703042268, 0.0, 596.7783523710964], [0.0, 1216.2799457964493, 257.77238817119604], [0.0, 0.0, 1.0]])
D=np.array([[-0.126503993300498], [0.03688655131559319], [0.3498539558136208], [-2.006807518705875]])

def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    start_time = time.perf_counter()
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print("Finished in {} secs".format(round(run_time, 3)))
    cv2.imshow("undistorted", undistorted_img)
    cv2.imwrite("./720p_undistorted/"+img_path.split("\\")[-1], undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)