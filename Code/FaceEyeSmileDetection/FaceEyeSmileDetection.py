import cv2

#Cascade File
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml");
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml");

#Capturing video through Webcam / Pi Camera
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, img = cap.read()
        if ret == True:
#converting frame(img i.e BGR) to gray Image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
#Detects for the Face features
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(img,"Face",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
#After detecting the Face it finds for the Eye features with in the Area
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    cv2.putText(img,"Eye",(x+ex,y+ey),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))

#After detecting the Face it finds for the Smile features with in the Area
                smile = smile_cascade.detectMultiScale(roi_gray,scaleFactor=1.3,minNeighbors=22,minSize=(25, 25))
                for (sx,sy,sw,sh) in smile:
                    cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,255,255),2)
                    cv2.putText(img,"Smile",(x+sx,y+sy),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255))
                    
            cv2.imshow('img',img)

#Press Esc for closing the program
            if cv2.waitKey(1) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
        
if __name__ == '__main__':
    main()