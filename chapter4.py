import cv2 as c
import numpy as np

# create images with matrix

# img = np.full((1080, 1920, 3), 0, np.float64)
# # img=np.zeros((720, 1280))

# img[0:360,0:640]=0, 100, 100
# img[360:720,640:1280]=0, 100, 100
# img[0:360, 640:1280]=100, 100, 0
# img[360:720, 0:640]=100, 100, 0

# while True:
#     c.imshow("Image", img)
#     if c.waitKey(1) & 0xFF==ord('q'):
#         c.destroyAllWindows()
#         break

# drawing line

# img=np.full((720, 1280, 3), 0, np.float64)
# # img[:, :]=255, 153, 10

# c.line(img, (0,0), (img.shape[1], img.shape[0]), (100,100,0), 3)
# c.line(img, (0,720), (1280, 0), (100,100,0), 3)
# c.line(img, (640,0), (640, 720), (100,100,0), 3)
# c.line(img, (640,0), (640, 720), (100,100,0), 3)
# c.line(img, (0,360), (1280, 360), (100,100,0), 3)

# while True:
#     c.imshow("Image", img)
#     if c.waitKey(1) & 0xFF==ord('q'):
#         c.destroyAllWindows()
#         break

# drawing rectangle

img = np.zeros((720, 1280, 3), np.float64)

c.rectangle(img, (100,100), (300, 300), (0, 255, 0), 2) # a rectangle
c.rectangle(img, (300,300), (500, 500), (0, 255, 255), c.FILLED) # a filled rectangle
c.circle(img, (300, 300), 283, (255, 0, 255), 2) # a circle
c.putText(img, "A rectangle, a filled", (600, 300), c.FONT_HERSHEY_COMPLEX, 1, (230, 221, 0), 2) # puttext on the image
c.putText(img, "rectangle and a circle around them", (600, 350), c.FONT_HERSHEY_COMPLEX, 1, (230, 221, 0), 2) # to put the next in the new line

while True:
    c.imshow("Image", img);
    if c.waitKey(1) & 0xFF==ord('q'):
        c.destroyAllWindows()
        break