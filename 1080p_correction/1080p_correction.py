import numpy as np
import cv2
import sys
# You should replace these 3 lines with the output in calibration step
DIM=(1920, 1080)
K=np.array([[1817.4001408594697, 0.0, 901.0415973349199], [0.0, 1816.802874739775, 427.748840911313], [0.0, 0.0, 1.0]])
D=np.array([[-0.09158464867429174], [-0.7713521314752757], [5.9148331238833345], [-14.775237511386232]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.imwrite("./1080p_undistorted/"+img_path.split("\\")[-1], undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)