#!/usr/bin/python

import serial, time
#from serial import serial

#initialization and open the port
#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()

#ser.port = "/dev/ttyUSB0"
ser.port = "/dev/ttyO1"
#ser.port = "/dev/ttyS2"

ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits

#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read

ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

ser.writeTimeout = 2     #timeout for write

try: 

    ser.open()

except Exception, e:

    print "error open serial port: " + str(e)

    exit()
if ser.isOpen():
    try:
        ser.flushInput() # flush input  buffer
        ser.flushOutput() # flush output buffer
    except Exception.e1:
        print "error to open serial port"
    
    ser.write("I'm BeagleBone Black! line one\n")
    ser.write("I'm BeagleBone Black! line two\n")
    print("write data: I'm BeagleBone Black!")
    time.sleep(0.5)  #give the serial port sometime to receive the data

    while True:
        data=ser.readline();
        print(data)

else:
    print "can't open serial port"
