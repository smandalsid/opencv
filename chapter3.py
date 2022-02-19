import cv2 as c

img=c.imread("IMG_0214.JPEG")

height=int(img.shape[0]*.3)
width=int(img.shape[1]*.3)

img1=c.resize(img, (width, height))

cropped=img1[123:603, 62:375] # height first width second

while True:
    # c.imshow("Image", img1)
    c.imshow("Image", cropped)
    if c.waitKey(1) & 0xFF==ord('q'):
        c.destroyAllWindows()
        break