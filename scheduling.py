

class User:
	def __init__(userID, name, email):
		UserID = userID
		Name = name
		Email = email 

class Appointment: 
	def __init__(appointmentID, isFlexible, userID, title, location, invitees, notes, alert, isComplete):
		AppointmentID = appointmentID
		isFlexible = isFlexible
		UserID = userID
		Title = title
		Location = location
		Invitees = invitees
		Notes = notes
		Alert = alert
		isComplete = isComplete

class TimeSlot: 
	def __init__(timeSlotID, appointmentID, startTime, endTime):
		TimeSlotID = timeSlotID
		AppointmentId = appointmentID
		StartTime = startTime
		EndTime = endTime


class Flexible:
	def __init__(flexibleID, startDate, endDate, hours):
		FlexibleID = flexibleID
		StartDate = startDate
		EndDate = endDate
		Hours = hours

class NotFlexible: 
	def __init__(nonFlexibleID, date, startTime, endTime):
		NonFlexibleID = nonFlexibleID
		Date = date
		StartTime = startTime
		EndTime = endTime



