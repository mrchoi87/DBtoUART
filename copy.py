import serial
import time

ser1 = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while True:
#     if ser.readable():
#         res = ser.read(ser.inWaiting())

#     print("rx: " + str(ser1.readline()))

     ser1.write('v_Temp.val=30\xff\xff\xff')
     ser1.write('v_O2.val=20\xff\xff\xff')
     time.sleep(1)	
#     ser1.write('\xff\xff\xff')
#    Data_rx=codecs.encode(tmp2, 'hex')
#    print("rx:" + str(Data_rx))
