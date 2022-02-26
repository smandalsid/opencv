import numpy as np
import cv2 as c

img=c.imread("tree.png")
# height=int(.4*img.shape[0])
# width=int(.4*img.shape[1])
# img=c.resize(img, (width, height))

while True:
    c.imshow("Pic", img)
    if c.waitKey(1) & 0xFF==ord('q'):
        c.destroyAllWindows()
        break