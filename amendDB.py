import sqlite3
import sortingfns
import available_slots
import datetime
from datetime import timedelta
import math
#from datetime import datetime

def add_user( username, email ): 
	# connecting to the database  
	connection = sqlite3.connect("Planner.db") 
	# cursor  
	crsr = connection.cursor() 
	command = "INSERT INTO User ( Name, Email ) VALUES ( \"" + str(username) + "\", \"" + str(email) + "\");"
	crsr.execute(command)  
	connection.commit() 
	# close the connection 
	connection.close()

def add_flexible( appointmentid, startdate, enddate, noofhours ):
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "INSERT INTO Flexible (AppointmentID, StartDate, EndDate, NoOfHours) VALUES( "
	command += str(appointmentid) + ", \"" + str(startdate)
	command += "\", \"" + str(enddate) + "\", " + str(noofhours) + " );"
	crsr.execute(command)  
	connection.commit() 
	# close the connection 
	connection.close()

def add_notflexible( appointmentid, date, starttime, endtime ):
	# connecting to the database  
	connection = sqlite3.connect("Planner.db") 
	# cursor  
	crsr = connection.cursor() 
	command = "INSERT INTO NotFlexible (AppointmentID, DateOfAppointment, StartTime, EndTime) VALUES( " 
	command += str(appointmentid) + ", \"" + str(date) + "\", "
	command += "\"" + str(starttime) + "\", \"" + str(endtime) + "\" );"
	crsr.execute(command)  
	connection.commit() 
	# close the connection 
	connection.close()

def add_timeslot( userid, appointmentid, date, starttime, endtime): 
	# connecting to the database  

	print("CALLED ADD TIMESLoT")
	connection = sqlite3.connect("Planner.db") 
	# cursor  
	crsr = connection.cursor() 
	command = "INSERT INTO TimeSlot (UserID, AppointmentID, DateOfAppointment, StartTime, EndTime) VALUES( " 
	command += str(userid) + ", " + str(appointmentid) + ",\"" +  str(date) + "\", " 
	command += "\"" + str(starttime) + "\", \"" + str(endtime) + "\" );"
	crsr.execute(command)  
	connection.commit() 
	# close the connection 
	connection.close()

def delete_user( userid ):  
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "DELETE FROM User WHERE UserID = " + str(userid) + ";"
	crsr.execute(command)  
	connection.commit() 
	connection.close()

def delete_flexible( appointmentid ):  
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "DELETE FROM Flexible WHERE AppointmentID = " + str(appointmentid) + ";"
	crsr.execute(command)  
	connection.commit() 
	connection.close()

def delete_notflexible( appointmentid ):  
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "DELETE FROM NotFlexible WHERE AppointmentID = " + str(appointmentid) + ";"
	crsr.execute(command)  
	connection.commit() 
	connection.close()

def delete_timeslot( appointmentid ):  
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "DELETE FROM TimeSlot WHERE AppointmentID = " + str(appointmentid) + ";"
	crsr.execute(command)  
	connection.commit() 
	connection.close()


def add_appointment( userid, title, isflexible, iscomplete, notes, alert, invitees, location, start, end, hours, date ): 
	#print("called")
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "INSERT INTO Appointment (UserID, Title, isFlexible, isComplete, Notes, Alert, Invitees, Location) VALUES ( "
	command += str(userid) + ", \"" + str(title) + "\", " + str(isflexible) 
	command += ", " + str(iscomplete) + ", \"" + str(notes) + "\", \"" + str(alert) + "\", " 
	command += str(invitees) + ", \"" + str(location) + "\");"
	crsr.execute(command) 
	connection.commit() 
	connection.close()

	connection2 = sqlite3.connect("Planner.db") 
	crsr2 = connection2.cursor() 
	command = "SELECT MAX(AppointmentID) FROM Appointment;"
	AppointmentID = crsr2.execute(command)
	rows = crsr2.fetchall()
	connection2.commit() 
	connection2.close()
	row = rows[0]

	if isflexible == 1: #it is flexible
		add_flexible( rows[0][0], start, end, hours )
		generate_timeslot (userid, rows[0][0], start, end, hours)
	else: #it is not flexible
		add_notflexible( rows[0][0], date, start, end )
		add_timeslot(userid, rows[0][0], date, start, end )

	#print("done")


def delete_appointment( appointmentid ): 
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "SELECT isflexible FROM Appointment WHERE AppointmentID = " + str(appointmentid) + ";"
	crsr.execute(command) 
	rows = crsr.fetchall()
	isflexi = rows[0][0]
	connection.commit() 
	connection.close()
	#print(rows)
	if isflexi == 0: 
		delete_notflexible( appointmentid )
	else:
		delete_flexible( appointmentid )
	delete_timeslot( appointmentid )
	#delete_app( appointmentid )

	command2 = "DELETE FROM Appointment WHERE AppointmentID = " + str(appointmentid) + ";"
	connection2 = sqlite3.connect("Planner.db") 
	crsr2 = connection2.cursor() 
	crsr2.execute(command2) 
	connection2.commit() 
	connection2.close()

def generate_timeslot( userid, appointmentid, start, end, hours):

 connection = sqlite3.connect("Planner.db") 
 crsr = connection.cursor()
 command = "SELECT * FROM TimeSlot WHERE UserID = " + str(userid) + ";"
 crsr.execute(command)
 rows = crsr.fetchall()
 connection.commit() 
 connection.close()
 info1 = []
 info = []
 for i in rows:
 	temp_date = str(i[3])
 	temp_start = str(start)
 	temp_end = str(end)
 	if (temp_date >= temp_start) and (temp_date <= temp_end):
 		info1.append(i)

 info = [list(ele) for ele in info1]
 info = sortingfns.selectionSort(info)
 info = sortingfns.selectionSort1(info)
 get_slots(info, hours, userid, appointmentid, start, end)


def get_slots(array, hours, userid, appointmentid, startDate, endDate):
	
	daysinMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
	remaining_hours = hours
	year = int(startDate.year)
	print("year", year)
	ts_from_db_array = array 
	

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
			hoursbooked = 0			

			maxhours_inday = float(hours) / (float(rangeEnd) - float(rangeStart) + float(1.0))

			all_available_slots = sortingfns.initslotarray()
			array_for_ts_of_curr_day =[] 
			curr_date_str = ""
			for i in range(0, len(ts_from_db_array)): 
				curr_date_str = ts_from_db_array[i][3]
				curr_date = curr_date_str[-2:]
				curr_date = int(curr_date)
				if( curr_date == day):
					array_for_ts_of_curr_day.append(ts_from_db_array[i])

			for ts in array_for_ts_of_curr_day: 
#				starting = datetime.datetime.strptime(ts[4], '%H:%M:%S').time()
#				ending = datetime.datetime.strptime(ts[5], '%H:%M:%S').time()
				starting = sortingfns.sroundoff( datetime.datetime.strptime(ts[4], '%H:%M:%S').time() )
				ending = sortingfns.eroundoff( datetime.datetime.strptime(ts[5], '%H:%M:%S').time() )
				start_ctr = 0 
				end_ctr = 0 

				for i in range(0, len(all_available_slots)): 
					if( all_available_slots[i].startTime == starting): 
						start_ctr = i
					if( all_available_slots[i].endTime == ending): 
						end_ctr = i 	

				for i in range(start_ctr, end_ctr+1): 
					all_available_slots[i].free = False

				#Blocking 1 hour for lunch
				all_available_slots[7].free = False
				all_available_slots[8].free = False
						
			for i in range(0, len(all_available_slots)-1): 
				if( all_available_slots[i].free == True and all_available_slots[i+1].free == True): 
					all_available_slots[i].free = False
					all_available_slots[i+1].free = False
					hoursbooked = hoursbooked + 1

					if(remaining_hours > 0 and hoursbooked <= math.ceil(maxhours_inday)): 
						add_timeslot( userid, appointmentid, datetime.date(year, month, day), (all_available_slots[i].startTime).strftime('%H:%M:%S'), (all_available_slots[i+1].endTime).strftime('%H:%M:%S'))
						remaining_hours = remaining_hours - 1

			
add_appointment( 1, "New code test", 1, 0, "testing datetime", datetime.datetime(2020, 2, 17, 14, 15, 0), 3, "bombay", 
	datetime.date(2020, 2, 17), datetime.date(2020, 2, 20), 15, " ")

#for i in range(17, 30): 
	#delete_appointment(i)
#delete_appointment(32)


