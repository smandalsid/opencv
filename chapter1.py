import cv2

# FOR IMAGE

# img=cv2.imread('IMG_0214.JPEG') # used to read an image
# cv2.imshow("OUTPUT", img) # to show the image, first arg is window name, second arg if for the image we want to display
# cv2.waitKey(10000) # to keep the image opened in miliseconds time, 0 means infinite

# FOR VIDEO

# cap=cv2.VideoCapture("video.mp4") # a video is a series of frames
# while True:
#     success, img=cap.read() # we read every frame in a while loop, success tells if the frame was obtained successfully or not, and img stores the frame
#     cv2.imshow("Video", img)
#     if cv2.waitKey(15) and 0xFF==ord('q'):
#         break

# FOR CAMERA

cap=cv2.VideoCapture(0)
cap.set(3, 640) # id 3 is to set the width of the window
cap.set(4, 480) # id 4 is to set the height of the window
cap.set(10, 150) # id 10 is to set the brightness of the image captured

while True:
    success, img = cap.read()
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break