import cv2
face_caascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Your webcam is not opening, try smacking it with an iron axe or shooting it with an AK47")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print("Your camera is working but unable to use maybe because its useless.")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_caascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,f"total people count{len(faces)}",(10,30),font,1,(0,0,0),3)
    cv2.imshow("faces detected",frame)
    if cv2.waitKey(15000):
        break
cap.release()
cv2.destroyAllWindows()


