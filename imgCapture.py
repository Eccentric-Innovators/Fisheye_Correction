import cv2
import config

def captureImg(src, dest, quality):
    cam = cv2.VideoCapture(src)
    cam.set(3,config.qualities[quality][0])
    cam.set(4,config.qualities[quality][1])
    cv2.namedWindow("Camera")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("Camera", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = dest.format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()