import serial

#COM port of the reciever
Serial_port='COM2'
ser = serial.Serial(Serial_port, 9600, timeout=1) #opening and connecting the port
print("Recieving on"+Serial_port)

while True:
    line = ser.readline().decode() #recieving data fron esp32
    #decoding so that it recieves in the form of string
    print(str(line))
    
