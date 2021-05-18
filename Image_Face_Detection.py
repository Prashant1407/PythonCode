import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
print(face_cascade) # print adderess of casecade file.

img = cv2.imread("HumanFace.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors =5)
eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors =5)

print(type(faces))
print(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255),2)
    
for (ex,ey,ew,eh) in eyes:
    img = cv2.rectangle(img, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()



