import cv2

#Cascade File
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

#Capturing video through Webcam / Pi Camera
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, img = cap.read()
        if ret == True:
#converting frame(img i.e BGR) to gray Image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)     
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(img,"Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
                    
            cv2.imshow('img',img)
            
#Press Esc for closing the program
            if cv2.waitKey(20) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
        
if __name__ == '__main__':
    main()
