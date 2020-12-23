import cv2
face_cascade=cv2.CascadeClassifier('face_data.xml')
img=cv2.imread('mannu.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
cv2.imshow('Face Recognition',img)
cv2.waitKey()