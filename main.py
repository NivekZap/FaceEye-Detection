import cv2
#tenemos que asegurarnos que los archivos de haarcascade esten correctamente localizados en las carpetas
face_cascade = cv2.CascadeClassifier('C:/Users/pazsa/Desktop/python projects/video/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/pazsa/Desktop/python projects/video/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Error: No se pudo capturar la imagen.")
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    cv2.imshow('img', img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:  
        break

cap.release()
cv2.destroyAllWindows()





