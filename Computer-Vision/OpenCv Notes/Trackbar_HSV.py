import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing(x):
    pass

cv2.namedWindow("Trackbar") 
cv2.resizeWindow("Trackbar",500,500)

cv2.createTrackbar("Lower - H", "Trackbar", 0,180, nothing)
cv2.createTrackbar("Lower - S","Trackbar",0,255, nothing)
cv2.createTrackbar("Lower - V","Trackbar", 0,255, nothing)



cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper - S","Trackbar", 0,255, nothing)
cv2.createTrackbar("Upper - V","Trackbar", 0,255 , nothing)

cv2.setTrackbarPos("Upper - H","Trackbar",180)
cv2.setTrackbarPos("Upper - S","Trackbar",255)
cv2.setTrackbarPos("Upper - V","Trackbar",255)

while True:
    ret,frame = cap.read()
   
    frame = cv2.flip(frame,1)
    frame_2 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H","Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S","Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - H","Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H","Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S","Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V","Trackbar")

    lower_color = np.array([lower_h,lower_s,lower_v])
    upper_color = np.array([upper_h,upper_s,upper_v])

    mask = cv2.inRange(frame_2,lower_color,upper_color)

    cv2.imshow("Webcam",frame)
    cv2.imshow("HSV",mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()