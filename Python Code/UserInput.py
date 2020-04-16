import amendDB
import sqlite3

def identifyUser( name ):
	command = "SELECT UserID from User WHERE Name = \"" + name + "\";"
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	crsr.execute(command) 
	rows = crsr.fetchall()
	connection.commit() 
	connection.close()
	if rows != []:
		UserID = rows[0][0]
		print( "UserID = ", UserID)
		return 1, UserID
	else: 
		print("This user does not exist, try again!")
		return 0, 0

def displayUser( userid ): 
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "SELECT * from User WHERE UserID = " + str(userid) + ";"
	crsr.execute(command) 
	rows = crsr.fetchall()
	connection.commit() 
	connection.close()

	print( "\nWelcome " + rows[0][1] + "!! \nUserID: " + str(rows[0][0]) +
		"\nEmail: " + rows[0][2])

def displayInfo (title, location, isFlexible, notes, invitees ): 
	print("\nTitle: " + title + "\n" +
		"Location: " + location + "\n" +
		"Flexible (0/1): " + str(isFlexible) + "\n" +
		"Notes: " + notes + "\n" + 
		"Invitees: " + invitees + " \n" )

def inputFlexible(): 
	print("\nInput Task Details: \n")
	startdate = input( "Enter start date of task: ")
	enddate = input( "Enter end date of task: ")
	hours = input( "Enter number of hours of task: ")
	print("\nStart Date: " + str(startdate) +"\n" + 
		"End Date: " + str(enddate) + "\n" + 
		"Total hours: " + str(hours) + "\n")
	return startdate, enddate, hours

def inputNotFlexible(): 
	print("\nInput Appointment Details: \n")
	date = input( "Enter date of appointment: ")
	starttime = input( "Enter start time of appointment: ")
	endtime = input( "Enter end time of appointment: ")
	print("\nDate: " + str(date) +"\n" + 
		"Start Time: " + str(starttime) + "\n" + 
		"End Time: " + str(endtime) + "\n")
	return date, starttime, endtime

def addAppointment():
	flag = 0
	while flag==0: 
		name = input( "Enter your name: ")
		flag, userid = identifyUser( name )
	displayUser( userid )

	title = ""
	location = ""
	isFlexible = ""
	notes = ""
	invitees = ""

	title = input( "Enter the title: ")
	displayInfo( title, location, isFlexible, notes, invitees )
	location = input( "Enter the location: ")
	displayInfo( title, location, isFlexible, notes, invitees )
	isFlexible = input( "Enter if your appointment is Flexible (1) or not (0): ")
	isFlexible = int(isFlexible)
	displayInfo( title, location, isFlexible, notes, invitees )
	notes = input( "Enter your notes: ")
	displayInfo( title, location, isFlexible, notes, invitees )
	invitees = input( "Enter the name of your invitee: ")
	var, inviteeid = identifyUser(invitees)
	displayInfo( title, location, isFlexible, notes, invitees )
	hours = 0
	date = "0"
	if isFlexible == 0: #not flexible 
		date, start, end = inputNotFlexible()
	else: 
		start, end, hours = inputFlexible() 

	amendDB.add_appointment(userid, title, isFlexible, 0, notes, "0", int(inviteeid), location, start, end, hours, date )

def deleteAppointment(): 
	print("\nYou have chosen to delete an existing appointment!")
	appid = input("Enter the appointment id of the appointment you want to delete: ")
	amendDB.delete_appointment( int(appid ) )


def addUser():
	print("\nYou have chosen to add a new user!")
	name = input("Enter the name: ")
	email = input("Enter the email: ")
	amendDB.add_user(name, email)

	command = "SELECT UserID from User WHERE Name = \"" + name + "\";"
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	crsr.execute(command) 
	rows = crsr.fetchall()
	connection.commit() 
	connection.close()
	if rows != []:
		UserID = rows[0][0]
		print( "UserID = ", UserID)

	print("Congratulations! " + name + " has been added to the database. " + 
		"The user id is " + str(UserID) )

def deleteUser(): 
	print("\nYou have chosen to delete an existing user!")
	userid = input("Enter the userid you want to delete: ")
	connection = sqlite3.connect("Planner.db") 
	crsr = connection.cursor() 
	command = "SELECT * from User WHERE UserID = " + str(userid) + ";"
	crsr.execute(command) 
	rows = crsr.fetchall()
	connection.commit() 
	connection.close()
	if rows != []: 	#userid exists 
		UserID = rows[0][0]
		amendDB.delete_user( UserID )
		print("User with user id = " + str(UserID) + " has been deleted! ")
	else: 
		print("This user does not exist, try again!")
	



def takeInput2(): 
	print( "\nWelcome to Planner.ai!! ")
	print( "\nPress 1 to add a new user \nPress 2 to delete a user " + 
		 "\nPress 3 to add appointment \nPress 4 to delete appointment " + 
		 "\nPress 5 to view calendar \nPress 0 to exit")
	flag = input("Enter your choice: ")
	flag = int( flag )
	while flag != 0:
		if flag == 1: 
			addUser()
		elif flag == 2: 
			deleteUser()
		elif flag == 3: 
			addAppointment()
		elif flag == 4: 
			deleteAppointment()
		elif flag == 5: 
			print("\nComing soon, stay tuned! ")
		elif flag == 0: 
			exit(0)
		flag = input("\nEnter your choice: ")
		flag = int(flag)




takeInput2()

