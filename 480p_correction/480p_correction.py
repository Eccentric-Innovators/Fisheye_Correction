import numpy as np
import cv2
import sys
# You should replace these 3 lines with the output in calibration step
DIM=(640, 480)
K=np.array([[801.8341453085372, 0.0, 297.382045200608], [0.0, 803.5365907221694, 184.737717672594], [0.0, 0.0, 1.0]])
D=np.array([[-0.08317377936964446], [-1.1519014960897285], [12.256778062202248], [-40.77008758513109]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.imwrite("./480p_undistorted/"+img_path.split("\\")[-1], undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)