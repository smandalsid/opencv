import cv2

# CREATE A GRAYSCALE IMAGE

img = cv2.imread("IMG_0214.JPEG")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # to onvert the color of the image, to grayscale

width=int(imgGray.shape[1]*.40) #scalethe image width
height=int(imgGray.shape[0]*.40)
# scale the image height
dim=(width, height)
#dimension of the picture
# resize the image according to the dimension
imgGray=cv2.resize(imgGray, dim)


while True:
    # show the image
    cv2.imshow("Grayscale image", imgGray)
    # save the image
    cv2.imwrite("grayscale.png", imgGray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break