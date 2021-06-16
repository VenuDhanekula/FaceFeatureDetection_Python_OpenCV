import cv2

#Cascade File
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml");

#Capturing video through Webcam / Pi Camera
cap = cv2.VideoCapture(0)

def main():
    while True:
        ret, img = cap.read()
        if ret == True:
#converting frame(img i.e BGR) to gray Image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            smile = smile_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=22,minSize=(25, 25))
                
#Detects for the Smile features
            for (sx,sy,sw,sh) in smile:
                cv2.rectangle(img,(sx,sy),(sx+sw,sy+sh),(0,255,255),2)
                cv2.putText(img,"Smile",(sx,sy),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255))
                    
            cv2.imshow('img',img)
            
#Press Esc for closing the program
            if cv2.waitKey(1) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
        
if __name__ == '__main__':
    main()

