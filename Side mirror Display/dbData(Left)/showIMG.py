import requests
from Tkinter import *
from PIL import ImageTk, Image

def changeImg(imgLabel):
    def change(): 
        URL = "http://192.168.0.14:3001/Distance"
        res = requests.get(URL)
        #outData type -> List
        outData = res.json()
	outData = outData[0]
        #dictData type -> Dic
        dictData = outData[0]
        #find key (Left -> LeftDistance , Right->RightDistance)
        printData = dictData['leftDistance']
    
        if printData<15.0:
            img = ImageTk.PhotoImage(Image.open("L_1.jpg"))
            print("warning zone")

        elif printData>15.0 and printData<40.0 :
            img = ImageTk.PhotoImage(Image.open("L_2.jpg"))
            print("caution zone")

        else :
            img = ImageTk.PhotoImage(Image.open("L_3.jpg"))    
            print("safe zone")

        imgLabel.configure(image = img)
        imgLabel.image = img
        imgLabel.after(100, change)  
    change()        

my_gui = Tk()
my_gui.resizable(width=True, height=True)
imgLabel = Label(my_gui)
imgLabel.pack()
changeImg(imgLabel)
my_gui.mainloop()
