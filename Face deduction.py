import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Reading the image as it is
img = cv2.imread("people.jpg")

# Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

for x, y, w, h in faces :
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/2)))

cv2.imshow("Gray", img)

cv2.waitKey(0)







