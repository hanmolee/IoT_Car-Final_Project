import requests
from Tkinter import *
from PIL import ImageTk, Image

def changeImg(imgLabel):
    def change(): 
        URL = "http://192.168.0.14:3001/distance"
        res = requests.get(URL)
        #outData type -> List
        outData = res.json()
        print(outData)
	outData = outData[0]
 	print("change->",outData)
        #dictData type -> Dic
        dictData = outData[0]
        #find key (Left -> LeftDistance , Right->RightDistance)
        printData = dictData['rightDistance']
    	print("right",printData)
        if printData<15.0:
            img = ImageTk.PhotoImage(Image.open("R_1.jpg"))
            print("warning zone")

        elif printData>15.0 and printData<40.0 :
            img = ImageTk.PhotoImage(Image.open("R_2.jpg"))
            print("caution zone")

        else :
            img = ImageTk.PhotoImage(Image.open("R_3.jpg"))    
            print("safe zone")

        imgLabel.configure(image = img)
        imgLabel.image = img
        imgLabel.after(1, change)  
    change()        

my_gui = Tk()
my_gui.resizable(width=True, height=True)
imgLabel = Label(my_gui)
imgLabel.pack()
changeImg(imgLabel)
my_gui.mainloop()
