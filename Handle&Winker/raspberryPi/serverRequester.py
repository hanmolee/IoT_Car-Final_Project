import serial
import time
import requests
 
 
def onInputTime():
    inputTime = time.strftime('%Y-%m-%d %H:%M:%S')
    print(type(inputTime))
    return inputTime
 
output = 0
 
while(1):
    try:
        ser = serial.Serial("/dev/ttyACM0",baudrate=9600)
        readValue =ser.readline()
        print("----------------------------")
        print(readValue)
        print("----------------------------")
 
   value = readValue[0]
        handle = readValue[1]
 
        try:
            ser.close()
            if(value!=output):
                output=value
                data = {'Value': output,'Time':onInputTime(),'Handle':handle}
                print("arduino Data is ->",data)
                URL = "http://192.168.0.14:3001/blinkers"
                response = requests.post(URL,data)
                print(response)
                response.close()
 
        except IndexError:
                print("Index Error")
    except serial.serialutil.SerialException:
            print("Seiral ERror")