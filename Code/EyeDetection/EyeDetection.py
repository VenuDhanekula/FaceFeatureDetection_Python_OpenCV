import cv2

#Cascade File
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml");

#Capturing video through Webcam / Pi Camera
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, img = cap.read()
        if ret == True:
#converting frame(img i.e BGR) to gray Image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            eyes = eye_cascade.detectMultiScale(gray)
                
#After detecting the face it checks for the eye features from the face area
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                cv2.putText(img,"Eye",(ex,ey),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
                    
            cv2.imshow('img',img)
            
#Press Esc for closing the program
            if cv2.waitKey(1) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
        
if __name__ == '__main__':
    main()
