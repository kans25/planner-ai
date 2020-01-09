import sqlite3
import scheduling

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
	# connecting to the database  
	connection = sqlite3.connect("Planner.db") 
	# cursor  
	crsr = connection.cursor() 
	command = "INSERT INTO Flexible (AppointmentID, StartDate, EndDate, NoOfHours) VALUES( "
	command += str(appointmentid) + ", " + str(startdate) + ", "
	command += ", " + str(enddate) + ", " + str(noofhours) + "\" );"
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
	command += str(appointmentid) + ", " + str(date) + ", "
	command += "\"" + str(starttime) + "\", \"" + str(endtime) + "\" );"
	crsr.execute(command)  
	connection.commit() 
	# close the connection 
	connection.close()

def add_timeslot( appointmentid, starttime, endtime): 
	# connecting to the database  
	connection = sqlite3.connect("Planner.db") 
	# cursor  
	crsr = connection.cursor() 
	command = "INSERT INTO TimeSlot (AppointmentID, StartTime, EndTime) VALUES( " 
	command += str(appointmentid) + ", " 
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


def add_appointment( userid, title, isflexible, iscomplete, notes, alert, invitees, location ): 
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "INSERT INTO Appointment (UserID, Title, isFlexible, isComplete, Notes, Alert, Invitees, Location) VALUES ( "
	command += str(userid) + ", \"" + str(title) + "\", " + str(isflexible) 
	command += ", " + str(iscomplete) + ", \"" + str(notes) + "\", " + str(alert) + ", " 
	command += str(invitees) + ", \"" + str(location) + "\");"
	crsr.execute(command) 
	connection.commit() 
	connection.close()

	# if isflexible == 1: #it is flexible
	# 	add_flexible( sp.flexibleid, appointmentid, sp.startdate, sp.enddate, sp.hours)
	# else: #it is not flexible
	# 	add_notflexible(sp.notflexibleid, appointmentid, sp.date, sp.starttime, sp.endtime)
	# 	add_timeslot(sp.timeslotid, appointmentid, sp.starttime, sp.endtime)


def delete_appointment( appointmentid ): 
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "SELECT isflexible FROM Appointment WHERE AppointmentID = " + str(appointmentid) + ";"
	isflexible = crsr.execute(command) 
	connection.commit() 
	connection.close()
	if isflexible == 0: 
		delete_notflexible( appointmentid )
	else:
		delete_flexible( appointmentid )
	delete_timeslot( appointmentid )
	delete_appointment( appointmentid )



add_user( "Kanaee", "kans@gmail.com")
add_user( "Rhea", "rhea@gmail.com")
#delete_user( 25 )





