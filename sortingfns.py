import sqlite3
import datetime
import available_slots
from datetime import timedelta
import calendar 


def selectionSort(array):
	n = len(array)
	for i in range(n):
		min_position = i 
		minimum_date = str(array[i][3])
		timeslot_id = array[i][0]
		user_id = array[i][1]
		appointment_id = array[i][2]
		start_time = str(array[i][4])
		end_time = str(array[i][5])
		for j in range(i+1, n):
			if (array[j][3] <= minimum_date):
				minimum_date = str(array[j][3])
				timeslot_id = array[j][0]
				user_id = array[j][1]
				appointment_id = array[j][2]
				start_time = str(array[j][4])
				end_time = str(array[j][5])
				min_position = j

		temp = str(array[i][3])
		temp1 = array[i][0]
		temp2 = array [i][1]
		temp3 = array[i][2]
		temp4 = str(array[i][4])
		temp5 = str(array[i][5])
		array[i][3] = minimum_date
		array[i][0] = timeslot_id
		array[i][1] = user_id
		array[i][2] = appointment_id
		array[i][4] = start_time
		array[i][5] = end_time
		array[min_position][0] = temp1
		array[min_position][1] = temp2
		array[min_position][2] = temp3
		array[min_position][3] = temp
		array[min_position][4] = temp4
		array[min_position][5] = temp5
	return array 



def selectionSort1(array):
	n = len(array)
	for i in range(n):
		min_position = i 
		date = str(array[i][3])
		timeslot_id = array[i][0]
		user_id = array[i][1]
		appointment_id = array[i][2]
		minimum_start_time = str(array[i][4])
		end_time = str(array[i][5])
		for j in range (i+1,n):
			if (str(array[i][3]) == str(array[j][3])):
				if (str(array[j][4]) < str(array[i][4])):
					min_position = j
					date = str(array[j][3])
					timeslot_id = array[j][0]
					user_id = array[j][1]
					appointment_id = array[j][2]
					minimum_start_time = str(array[j][4])
					end_time = str(array[j][5])

		temp = str(array[i][3])
		temp1 = array[i][0]
		temp2 = array [i][1]
		temp3 = array[i][2]
		temp4 = str(array[i][4])
		temp5 = str(array[i][5])
		array[i][3] = date
		array[i][0] = timeslot_id
		array[i][1] = user_id
		array[i][2] = appointment_id
		array[i][4] = minimum_start_time
		array[i][5] = end_time
		array[min_position][0] = temp1
		array[min_position][1] = temp2
		array[min_position][2] = temp3
		array[min_position][3] = temp
		array[min_position][4] = temp4
		array[min_position][5] = temp5
	return array 


def sum_time(time1,time2):
	FMT = '%H:%M:%S'
	timelist = []
	totalsecs = 0
	timelist.append(time1)
	timelist.append(str(time2))
	for tm in timelist:
		tm = str(tm)
		timeparts = [int(s) for s in tm.split(':')]
		totalsecs += (timeparts[0] * 60 + timeparts[1]) * 60 + timeparts[2]
	totalsecs, sec = divmod(totalsecs, 60)
	hr, minutes = divmod(totalsecs, 60)
	s =  "%d:%02d:%02d" % (hr, minutes, sec)
	return s 


def initslotarray(): 
	a = [] 
	for i in range(9,18): 
		for j in range(0,2): 
			if j == 0: 
				start_mins = 0
				end_mins = 30
				obj = available_slots.DaySlot(datetime.time(i, start_mins, 0), datetime.time(i, end_mins, 0), True)
			elif j == 1: 
				start_mins = 30
				end_mins = 0
				obj = available_slots.DaySlot(datetime.time(i, start_mins, 0), datetime.time(i+1, end_mins, 0), True)			
			a.append(obj)
	return a

def sroundoff( startTime ):
	#function to round down 
	startTime_str = str(startTime)
	hours = startTime_str[0:2]
	mins = startTime_str[3:5]
	secs = startTime_str[6:]
	if(mins >= '00' and mins <'30' ):
		startTime = datetime.time(int(hours), 0, 0)
	else: 
		startTime = datetime.time(int(hours), 30, 0)
	return (startTime) 

def eroundoff( endTime ): 
	#function to round up
	endTime_str = str(endTime)
	hours = endTime_str[0:2]
	mins = endTime_str[3:5]
	secs = endTime_str[6:]
	if(mins >'00' and mins <='30' ):
		endTime = datetime.time(int(hours), 30, 0)
	elif( mins >'30' and mins <='59') : 
		endTime = datetime.time((int(hours)+1), 0, 0)
	return(endTime)


def countTotalDays( array, hours, userid, appointmentid, startDate, endDate ): 
	daysinMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
	remaining_hours = hours
	year = int(startDate.year)
	print("year", year)
	if( calendar.isleap(year) ): 
		daysinMonth[1] = 29
	ts_from_db_array = array 
	counter = 0 

	for month in range(int(startDate.month), int(endDate.month)+1):
		print ("Current Month: ", month) 
		if (month == startDate.month) and (month == endDate.month) :
			rangeStart = startDate.day
			rangeEnd = endDate.day

		elif (month == startDate.month) and (month < endDate.month) :
			rangeStart = startDate.day
			rangeEnd = daysinMonth[month-1]

		elif (month > startDate.month) and (month < endDate.month):
			rangeStart = 1
			rangeEnd = daysinMonth[month-1]

		elif (month > startDate.month) and (month == endDate.month):
			rangeStart = 1
			rangeEnd = endDate.day


		for day in range(rangeStart,rangeEnd+1):
			counter = counter + 1 

	print( "counter", counter)

	return counter 



	