import cv2 as c
import numpy as np

img=c.imread("IMG_0214.JPEG")
height=img.shape[0]
width=img.shape[1]

width=int(.4*width)
height=int(.4*height)

img=c.resize(img, (width, height))

imghor=np.hstack((img, img))
imgver=np.vstack((img, img))

def stackimages(scale, imgs):
    finalimg=imgs[0]
    n=len(imgs)
    for i in range(1,n):
        imgs[i]=c.resize(imgs[i], (imgs[0].shape[1], imgs[0].shape[0]))
        finalimg=np.hstack((finalimg, imgs[i]))
    return finalimg


while True:
    # c.imshow("Horizontally stacked", imghor)
    # c.imshow("Vertically stacked", imgver)

    c.imshow("Stacking function", stackimages(1, [img, imgver]))
    if c.waitKey(1) & 0xFF==ord('q'):
        c.destroyAllWindows()
        break
