import serial
import time
import signal
import threading
import pymysql

exitThread = False

sensor_db = pymysql.connect(
		user = 'farmos',
		passwd = 'farmosv2@',
		host = '127.0.0.1',
		db = 'farmos',
		charset = 'utf8'
	)

cursor = sensor_db.cursor(pymysql.cursors.DictCursor)

sql_temp = "select nvalue from current_observations where data_id = 10000201"
sql_humi = "select nvalue from current_observations where data_id = 10000201"
sql_co2 = "select nvalue from current_observations where data_id = 10000201"
sql_o2 = "select nvalue from current_observations where data_id = 10000201"
sql_nh3 = "select nvalue from current_observations where data_id = 10000301"

def handler(signum, frame):
	exitThread = True

def readThread(ser):
	global exitThread

	while not exitThread:
		
		cursor.execute(sql_temp)
		value = cursor.fetchone()
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
	
		time.sleep(10)

if __name__ == "__main__":

	print("start")

	signal.signal(signal.SIGINT, handler)

	ser1 = serial.Serial(
		port = "/dev/ttyAMA0",
		baudrate = 9600,
		parity = serial.PARITY_NONE,
		stopbits = serial.STOPBITS_ONE,
		bytesize = serial.EIGHTBITS,
		timeout = 1
	)
	
	thread = threading.Thread(target = readThread, args = (ser1,))

	thread.start()
