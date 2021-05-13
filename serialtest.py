import serial
import time
import pymysql

ser1 = serial.Serial(
    port="/dev/ttyAMA0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

sensor_db = pymysql.connect(
     user = 'farmos',
     passwd = 'farmosv2@',
     host = '127.0.0.1',
     db = 'farmos',
     charset = 'utf8'
)

cursor = sensor_db.cursor(pymysql.cursors.DictCursor)
sql_temp = "select nvalue from current_observations where data_id = 10001001"
sql_humi = "select nvalue from current_observations where data_id = 10001001"
sql_co2 = "select nvalue from current_observations where data_id = 10001001"
sql_o2 = "select nvalue from current_observations where data_id = 10000201"
sql_nh3 = "select nvalue from current_observations where data_id = 10000101"
#sql = "select nvalue from current_observations where data_id%10 = 1"

while True:
#     print("rx: " + str(ser1.readline()))
     
     cursor.execute(sql_temp)	
     value = cursor.fetchone()
     print(value["nvalue"])	
     ser1.write('v_Temp.val=' + str(int(value["nvalue"])) + '\xff\xff\xff')

     cursor.execute(sql_humi)	
     value = cursor.fetchone()
     ser1.write('v_Humi.val=' + str(int(value["nvalue"])) + '\xff\xff\xff')

     cursor.execute(sql_co2)	
     value = cursor.fetchone()
     ser1.write('v_Co2.val=' + str(int(value["nvalue"])) + '\xff\xff\xff')

     cursor.execute(sql_o2)	
     value = cursor.fetchone()
     ser1.write('v_O2.val=' + str(int(value["nvalue"])) + '\xff\xff\xff')

     cursor.execute(sql_nh3)	
     value = cursor.fetchone()
     ser1.write('v_Nh3.val=' + str(int(value["nvalue"])) + '\xff\xff\xff')

#     ser1.write('v_O2.val=20\xff\xff\xff')
     time.sleep(1)	
