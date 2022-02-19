import cv2 as c

img=c.imread("cards.jpg")
width=int(img.shape[1]*.8)
height=int(img.shape[0]*.8)
dim=(width, height)
img=c.resize(img, dim)

width, height = 250, 350



while True:
    c.imshow("Cards", img)
    if c.waitKey(1) & 0xFF==ord('q'):
        c.destroyAllWindows()
        break