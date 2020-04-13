from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier =load_model(r'C:\Users\ritik\.spyder-py3\fer.h5')

lablesofclass = ['Angry','Happy','Neutral','Sad','Surprise']
cap = cv2.VideoCapture(0)



while True:
    
    r, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        rgray = gray[y:y+h,x:x+w]
        rgray = cv2.resize(rgray,(48,48),interpolation=cv2.INTER_AREA)  
	

        if np.sum([rgray])!=0:
            r = rgray.astype('float')/255.0
            r = img_to_array(r)
            r = np.expand_dims(r,axis=0)
            predicted = classifier.predict(r)[0]
            label=lablesofclass[predicted.argmax()]
            labelposition = (x,y)
            cv2.putText(frame,label,labelposition,cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),3)
        else:
            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),3)
    cv2.imshow('Emotion',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()