import cv2
import numpy as np

# CREATE A GRAYSCALE IMAGE

# img = cv2.imread("IMG_0214.JPEG")

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # to onvert the color of the image, to grayscale

# width=int(imgGray.shape[1]*.40) #scalethe image width
# height=int(imgGray.shape[0]*.40)
# # scale the image height
# dim=(width, height)
# #dimension of the picture
# # resize the image according to the dimension
# imgGray=cv2.resize(imgGray, dim)


# while True:
#     # show the image
#     cv2.imshow("Grayscale image", imgGray)
#     # save the image
#     cv2.imwrite("grayscale.png", imgGray)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         cv2.destroyAllWindows()
#         break



# BLUR AN IMAGE

img = cv2.imread("IMG_0214.JPEG")
kernel=np.ones((2,2),np.uint8)
kernel1=np.ones((1,1),np.uint8)

img0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # to onvert the color of the image, to grayscale
img1=cv2.GaussianBlur(img, (11, 11), 0)
img2=cv2.Canny(img, 100, 200)
imgDilate=cv2.dilate(img2, kernel, iterations=2)
imgErode=cv2.erode(img2, kernel1, iterations=1)

width=int(img1.shape[1]*.30) #scalethe image width
height=int(img1.shape[0]*.30)
# scale the image height
dim=(width, height)
#dimension of the picture
# resize the image according to the dimension
img=cv2.resize(img, dim)
img0=cv2.resize(img0, dim)
img1=cv2.resize(img1, dim)
img2=cv2.resize(img2, dim)
imgDilate=cv2.resize(imgDilate, dim)
imgErode=cv2.resize(imgErode, dim)


while True:
    # show the image
    cv2.imshow("Original image", img)
    cv2.imshow("Grayscale image", img0)
    cv2.imshow("Blurred image", img1)
    cv2.imshow("Canny image", imgDilate)
    # cv2.imshow("Eroded image", imgErode)
    # save the image
    # cv2.imwrite("grayscale.png", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break