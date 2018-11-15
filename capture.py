import cv2
import os


try:
    if not os.path.exists('test-data'):
        os.makedirs('test-data')
except OSError:
    print ('Error: Creating directory of data')

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 1

while True:

    ret, frame = cam.read()
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
        img_name = './test-data/'+"test"+str(img_counter) + '.jpg'
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()