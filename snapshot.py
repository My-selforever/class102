import cv2

def takeSs():
    oncam = cv2.VideoCapture(0)
    loop = True
    while (loop):
        read,frame=oncam.read()
        cv2.imwrite("UserImg.jpg",frame)
        print(read)
        loop=False

    oncam.release()
    cv2.destroyAllWindows()

print(takeSs())