import cv2
import numpy as np

cap = cv2.VideoCapture(0) #switching on webcam
back = cv2.imread('./image.jpg') #reading image.jpg

while cap.isOpened():
    #we'll take each frame
    ret, frame = cap.read()

    if ret:
        # how to convert rgb to hsv...using functoin cv2.cvtcolor(frame, cv2.COLORBGR2HSV)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)
        # how to get hsv values?
        # lower: hue - 10, 100, 100 higher: hue + 10, 255, 255
        green = np.uint8([[[0,255,0]]]) # [[[blue,green,red]]]
        hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
        # getting hsv value of green (u can also get red and blue)
        # print(hsv_green)
        # what we did, we got the lower value of green and upper value of green available in background
        # threshold the hsv to get only green values
        lower_green = np.array([0,100,100]) # lower is 0
        upper_green = np.array([70,255,255]) # we took 60 because the value of green is 60

        mask = cv2.inRange(hsv, lower_green, upper_green)
        # cv2.imshow("mask", mask)

        # part 1
        part1 = cv2.bitwise_and(back, back, mask=mask) # all things that are green
        # this will do AND operation of what all is green on webcam and mask it with "image.jpg" file
        # cv2.imshow("part1", part1)

        # we will take what all that is not green, ie not(mask)
        mask = cv2.bitwise_not(mask) # this will black-out all those parts which are not green

        # part 2
        part2 = cv2.bitwise_and(frame, frame, mask=mask) # all things that are not green
        # cv2.imshow("mask", part2)

        # what we want is part1 + part2 => show background + hide what all is green
        cv2.imshow("cloak", part1 + part2)
        # what is actually happening, we are taking live webcam + part1 (=> all things that are green) + mask (mark all those parts which are not green) + part2 (=> all those masked areas will be replaced with "image.jpg")

        if cv2.waitKey(1) == ord('q'):
            #if "q" is pressed
            break  # and breaking of video capturing

cap.release()
cv2.destroyAllWindows()