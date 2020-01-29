import sqlite3
import scheduling
import datetime

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

def add_timeslot( userid, appointmentid, starttime, endtime): 
	# connecting to the database  
	connection = sqlite3.connect("Planner.db") 
	# cursor  
	crsr = connection.cursor() 
	command = "INSERT INTO TimeSlot (UserID, AppointmentID, StartTime, EndTime) VALUES( " 
	command += str(userid) + ", " + str(appointmentid) + ", " 
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
	print("called")
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
	else: #it is not flexible
		add_notflexible( rows[0][0], date, start, end )
		add_timeslot(userid, rows[0][0], start, end )

	print("done")


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



add_user( "Keya", "keya@gmail.com")
add_user( "Rhea", "rhea@gmail.com")
add_user( "Kanaee", "kanaee@gmail.com")
add_appointment( 1, "Testing1", 0, 0, "testing datetime", datetime.datetime(2020, 1, 30, 14, 15, 0), 2, "ddun", 
	datetime.time(14, 30, 0), datetime.time(15, 30, 0), 0, datetime.date(2020, 1, 30))
add_appointment( 2, "Testing2", 1, 0, "testing datetime", datetime.datetime(2020, 1, 30, 14, 15, 0), 3, "bombay", 
	datetime.date(2020, 1, 30), datetime.date(2020, 2, 14), 12, " ")






