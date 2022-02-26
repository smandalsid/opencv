
# WARP PERSPECTIVE

import cv2 as c
import numpy as np
img=c.imread("cards.jpg")
width=int(img.shape[1]*.8)
height=int(img.shape[0]*.8)
dim=(width, height)
img=c.resize(img, dim)

width, height = 250, 350
pts1=np.float32([[642,88],[955,253],[387,607],[714,763]])
corners=np.float32([[0,0],[250,0],[0,350],[250,350]])

matrix=c.getPerspectiveTransform(pts1, corners)
img2=c.warpPerspective(img, matrix, (250, 350))




while True:
    c.imshow("Original Photo", img)
    c.imshow("Warp perspective of card", img2)
    if c.waitKey(1) & 0xFF==ord('q'):
        c.destroyAllWindows()
        break