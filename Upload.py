import dropbox
import cv2 
import time

startTime = int(time.time())

def takeSs():
    oncam = cv2.VideoCapture(0)
    loop = True
    while (loop):
        affix = int(time.time())
        read,frame=oncam.read()
        name = "Img"+affix+".jpg"
        cv2.imwrite(name,frame)
        print(read)
        loop=False
        startTime= int(time.time)
        
   
    oncam.release()
    cv2.destroyAllWindows()
    print("Success")
    return(name)

def upload(location):
    accesstoken="2t6SZd26whsAAAAAAAAAAZgM6fO5Jc6TqdjvzMSjTb3oM0fj7SVG2PvgM8gmH54d"
    fileto ='/Images/'+location
    filefrom = location
    dbox = dropbox.Dropbox(accesstoken)
    f = open(filefrom,'rb')
    dbox.files_upload(f.read(),fileto)
    print("Success2")

def main():
    print("in")
    loop = True
    imgs = 0
    while (loop and imgs<=5):
        print("hi")
        current = int(time.time())
        diff = current-startTime
        if(diff>=500 ):
            img= takeSs()
            upload(img)
            imgs+=1


main()