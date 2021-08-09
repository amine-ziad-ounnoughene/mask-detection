import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    test_image = frame
    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    grey = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    noses = nose_cascade.detectMultiScale(grey, 1.3, 5)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    if faces != ():
        for (x,y,w,h) in faces:
            i = 1
            cv2.rectangle(test_image,(x,y),(x+w,y+h),(255,0,0),2)
            face = test_image[y+2:y+h-2,x+2:x+w-2]
            i += 1
    
        
    if noses != ():
        p = 0
        for (x,y,w,h) in noses:
            p += 1
            cv2.rectangle(test_image,(x,y),(x+w,y+h),(255,0,0),2)
            nose = test_image[y+2:y+h-2,x+2:x+w-2]
            text = "no or incorrct mask"
            #cv2.putText(test_image,text,(x+w-70,y+h-70),4,0.3,(255,255,255))
            cv2.putText(test_image,text,(40,40),4,test_image.shape[0]  / test_image.shape[1],(255,255,255))
        cv2.putText(test_image,str(p)+" "+" of you is not wearing a mask",(100,100),4,test_image.shape[0]  / test_image.shape[1],(0,0,255))
        path = "censor-beep-2.mp3"
        import winsound

        winsound.Beep(1000, 100) 
         # Wait until sound has finished playing
    else:
        text = "wear mask"
        cv2.putText(test_image,text,(40,40),4,test_image.shape[0]  / test_image.shape[1],(0,0,255))
        
    cv2.imshow('frame', test_image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


