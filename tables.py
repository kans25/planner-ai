import sqlite3

# connecting to the database  
connection = sqlite3.connect("Planner.db") 
  
# cursor  
crsr = connection.cursor() 

# SQL command to create a table in the database 
sql_command_user = """CREATE TABLE User (  
UserID INTEGER PRIMARY KEY,  
Name VARCHAR(128), 
Email VARCHAR(128))"""
  
# SQL command to create a table in the database 
sql_command_appointment = """CREATE TABLE Appointment (  
AppointmentID INTEGER PRIMARY KEY,  
UserID INTEGER, 
Title VARCHAR(128), 
IsFlexible BIT, 
isComplete BIT, 
Notes VARCHAR(256), 
Alert DATE, 
Invitees INTEGER, 
Location VARCHAR(128), 
FOREIGN KEY(UserID) REFERENCES User(UserID) )"""

# SQL command to create a table in the database 
sql_command_timeslot = """CREATE TABLE TimeSlot (  
TimeSlotID INTEGER PRIMARY KEY, 
UserID INTEGER,
AppointmentID INTEGER, 
StartTime VARCHAR(128), 
EndTime VARCHAR(128), 
FOREIGN KEY(UserID) REFERENCES Appointment(UserID),
FOREIGN KEY(AppointmentID) REFERENCES Appointment(AppointmentID) )"""

# SQL command to create a table in the database 
sql_command_flexible = """CREATE TABLE Flexible (  
FlexibleID INTEGER PRIMARY KEY,
AppointmentID INTEGER, 
StartDate VARCHAR(128), 
EndDate VARCHAR(128),  
NoOfHours int,  
FOREIGN KEY(AppointmentID) REFERENCES Appointments(AppointmentID) )"""

# SQL command to create a table in the database 
sql_command_notflexible = """CREATE TABLE NotFlexible (  
NotFlexibleID INTEGER PRIMARY KEY,
AppointmentID INTEGER, 
DateOfAppointment VARCHAR(128),  
StartTime VARCHAR(128), 
EndTime VARCHAR(128),
FOREIGN KEY(AppointmentID) REFERENCES Appointments(AppointmentID) )"""

 
# execute the statement 

crsr.execute(sql_command_user) 
crsr.execute(sql_command_appointment) 
crsr.execute(sql_command_timeslot) 
crsr.execute(sql_command_flexible) 
crsr.execute(sql_command_notflexible) 

connection.commit() 
connection.close()