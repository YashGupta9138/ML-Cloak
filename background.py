import cv2
#this is my web-cam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    #here, we r reading from the webcam
    ret, back = cap.read() #cap.read will read frames from webcam and return it to ret & back, if false than it will return False
    if ret: #if ret == True
        #print(ret)
        cv2.imshow("image", back) #this will show image stored in back, back is what camera reading.
        if cv2.waitKey(1) == ord("q"): #if "q" is pressed
            #save the image
            cv2.imwrite('image.jpg', back) #just before "q" is pressed the image is captured
            break #and breaking of video capturing

cap.release()
cv2.destroyAllWindows()