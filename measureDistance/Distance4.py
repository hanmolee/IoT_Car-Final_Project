##-*- coding: utf-8 -*-
import serial
import datetime
import threading
import time
import requests
import re
 
#Queue Class
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
 
def insertDB():
    threading.Timer(0.5, insertDB).start()
 
    if(queue.size()==0):
        if(count==0):
	        arduinoThread = threading.Thread(target=arduinoOutput())	    
                global count
		count =1
	else:
	    	pass
 
    elif (queue.size()!=0) : 
        URL = "http://192.168.0.14:3001/distance"
        response = requests.get(URL)
	print("insertDB->F>DF>SFasdfadssd")
	print(response)	

	try:
	        print("----------------------------------------")

        	queueValue = queue.dequeue()
            #{'Front': ['23', '2017-07-06 19:14:18'], 'Right': ['4', '2017-07-06 19:14:18'], 'Left': ['29', '2017-07-06 19:14:18']}
            #print(inputValue) 
            # key value 
		print("pass")
       		for key in queueValue.keys():
	            print(key)
        	    inputVal = queueValue.get(key)
	            print(inputVal)
	            """
               		 Front 
	                ['23', '2017-07-06 19:20:04']
        	        Right
	                ['4', '2017-07-06 19:20:04']
                	Left
        	        ['92', '2017-07-06 19:20:04']
        	     """
        	    if (key == 'Front'):
               		 getFront = queueValue.get(key)
	               	 frontValue = getFront
 
	            elif (key == 'Right'):
	                getRight = queueValue.get(key)
	                rightValue = getRight
                
	            elif (key=='Left'):
	                getLeft = queueValue.get(key)
	                leftValue = getLeft
 
	            elif (key=='Time'):
	                getTime = queueValue.get(key)
	                checkTime = getTime
                    
 
	        data = {'checkTime': checkTime,'frontValue':frontValue,'rightValue':rightValue,'leftValue':leftValue}
	        print(data)
                
	        response = requests.post(URL,data)
        	print(response)
	        response.close()
        	print("----------------------------------------")        

	except:
		print("error")
            
        
  
def onInputTime():
    inputTime = time.strftime('%Y-%m-%d %H:%M:%S')
    print(type(inputTime))
    return inputTime
 
def arduinoOutput():
    threading.Timer(1.0, arduinoOutput).start()

    ser = serial.Serial("/dev/ttyACM0",baudrate=9600)

    value = ser.readline()
    print(value)
    inputTime = onInputTime()
    print(inputTime)
    data = value.split("/")


    data[1] = re.sub('[^0-9]','',data[1])
    data[3] = re.sub('[^0-9]','',data[3])
    data[5] = re.sub('[^0-9]','',data[5])


    try :   
    	print("data[1] -> ")
        print(data[1])
    	print("data[2] -> ")
    	print(data[3])
	print("data[5] -> ")
	print(data[5])

    	processData = { }
    
    	print("----------------------------------------")
    	processData['Front'] = data[1]
    	processData ['Right'] = data[3]
    	processData ['Left'] = data[5]
    	processData ['Time'] = inputTime            
    
    	print(processData)
    	queue.enqueue(processData)
    
    	print("queue size is :",queue.size())
    	print("----------------------------------------")
    	ser.close()

    except SerialException as e:
	print("SerialException")
    except IndexError:
	print("Index Error Arduino!!")
    
def main():
    global queue
    queue = Queue() 
    dbThread = threading.Thread(target=insertDB())        

count =0

main()
