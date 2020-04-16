#!/usr/bin/

import os
import time
import datetime
import MySQLdb

global c
global db

import sortingfns
import available_slots
import datetime
from datetime import timedelta
import math
import calendar

def add_user( username, email ): 
    print (username + " - " + email)
    sql =  "INSERT INTO User (Name, Email) VALUES (%s, %s)" 
    try:
        c.execute(sql,(str(username), str(email)))
        db.commit()
        print("User got added...")
    except:
        db.rollback()
        print("User got rolledbacked...")
    db.close()


def add_flexible( appointmentid, startdate, enddate, noofhours ):
    print(str(appointmentid) + " - " + startdate + " - " + enddate + " - " + noofhours)
    sql = "INSERT INTO Flexible (AppointmentID, StartDate, EndDate, NoOfHours) VALUES(%s, %s, %s, %s)"
    try:
        c.execute(sql,(str(appointmentid), str(startdate), str(enddate), str(noofhours)))
        db.commit()
        print("Flexible appointment got added...")
    except:
        db.rollback()
        print("Flexible appointment got rolledbacked...")
    # db.close()

def add_notflexible( appointmentid, date, starttime, endtime ):
    print (str(appointmentid) + " - " + date + " - " + starttime + " - " + endtime)
    sql =  "INSERT INTO NotFlexible (AppointmentID, DateOfAppointment, StartTime, EndTime) VALUES (%s, %s, %s, %s)" 
    try:
        c.execute(sql,(str(appointmentid), str(date), str(starttime), str(endtime)))
        db.commit()
        print("Not flexible appointment got added...")
    except:
        db.rollback()
        print("Not flexible appointment got rolledbacked...")
    #db.close()


def add_timeslot( userid, appointmentid, date, starttime, endtime): 
    print (str(userid) + " - " + str(appointmentid) + " - " + str(date) + " - " + str(starttime) + " - " + str(endtime))
    sql = "INSERT INTO TimeSlot (UserID, AppointmentID, DateOfAppointment, StartTime, EndTime) VALUES( %s, %s, %s, %s, %s)" 
    try: 
        c.execute(sql, (str(userid), str(appointmentid), str(date), str(starttime), str(endtime)))  
        db.commit() 
        print("Timeslot got added")
    except:
        db.rollback()
        print("Timeslot got rolledbacked...")
    # db.close()

def delete_user( userid ):  
    sql =  "DELETE FROM User WHERE UserID = %s" 
    try:
        c.execute(sql,(str(userid)))
        db.commit()
        print("User got deleted...")
    except:
        db.rollback()
        print("User got rolledbacked...")
    db.close()


def delete_flexible( appointmentid ): 
    sql =  "DELETE FROM Flexible WHERE AppointmentID = %s" 
    try:
        c.execute(sql, [appointmentid])
        db.commit()
        print("Flexible got deleted...")
    except:
        db.rollback()
        print("Flexible got rolledbacked...")
    # db.close()


def delete_notflexible( appointmentid ): 
    sql =  "DELETE FROM NotFlexible WHERE AppointmentID = %s" 
    try:
        c.execute(sql, [appointmentid])
        db.commit()
        print("NotFlexible got deleted...")
    except:
        db.rollback()
        print("NotFlexible got rolledbacked...")
    # db.close() 


def delete_timeslot( appointmentid ):  
    sql =  "DELETE FROM TimeSlot WHERE AppointmentID = %s" 
    try:
        c.execute(sql, [appointmentid] )
        db.commit()
        print("Timeslot got deleted...")
    except:
        db.rollback()
        print("Timeslot got rolledbacked...")
    # db.close()


def add_appointment( userid, title, isflexible, iscomplete, notes, alert, invitees, location, start, end, hours, date ): 
    sql = "INSERT INTO Appointment (UserID, Title, isFlexible, isComplete, Notes, Alert, Invitees, Location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        c.execute(sql,( str(userid), str(title), str(isflexible), str(iscomplete), str(notes), str(alert), str(invitees), str(location)))
        db.commit()
        print("Appointment got added...")

        try:
            c.execute("SELECT MAX(AppointmentID) FROM Appointment")      
            result = c.fetchall()
            if result is not None:
                appointmentid = result[0][0]

                if isflexible == "0": 
                    add_notflexible( appointmentid, date, start, end )
                    add_timeslot(userid, appointmentid, date, start, end )
                else: 
                    add_flexible( appointmentid, start, end, hours )
                    generate_timeslot(userid, appointmentid, start, end, hours)
        except:
            print ("read error")

    except: 
        db.rollback()
        print("Appointment got rolledbacked...")
    db.close()


def delete_appointment( appointmentid ): 

    sql = "SELECT isflexible FROM Appointment WHERE AppointmentID = %s"
    # sql =  "DELETE FROM User WHERE UserID = %s" 
    c.execute(sql, [appointmentid] ) 
    rows = c.fetchall()
    isflexi = rows[0][0]
    db.commit() 
    #print(rows)
    if isflexi == 0: 
        delete_notflexible( appointmentid )
    else:
        delete_flexible( appointmentid )
    delete_timeslot( appointmentid )
    #delete_app( appointmentid )

    sql2 = "DELETE FROM Appointment WHERE AppointmentID = %s"
    c.execute(sql2, [appointmentid]) 
    db.commit() 
    # db.close()


def generate_timeslot( userid, appointmentid, start, end, hours):
    sql = "SELECT * FROM TimeSlot WHERE UserID = %s "
    c.execute(sql, str(userid))
    rows = c.fetchall()
    db.commit() 
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
    print("REACHED HERE")
    get_slots(info, hours, userid, appointmentid, start, end)


def get_slots(array, hours, userid, appointmentid, startDate, endDate):

    totalNumOfDays = sortingfns.countTotalDays( array, hours, userid, appointmentid, startDate, endDate )
    
    daysinMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    remaining_hours = int(hours)
    startDate = sortingfns.strToDate(startDate)
    endDate = sortingfns.strToDate(endDate)

    year = int(startDate.year)
    print("year", year)
    if( calendar.isleap(year) ): 
        daysinMonth[1] = 29
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
            print("Day:", day)
            hoursbooked = 0         
            maxhours_inday = float(hours) / float(totalNumOfDays) 
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
#               starting = datetime.datetime.strptime(ts[4], '%H:%M:%S').time()
#               ending = datetime.datetime.strptime(ts[5], '%H:%M:%S').time()
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

    
def main():
    # add_user("name", "email@name.com")
    # delete_user(4)
    # add_appointment( 2, "testing flexible", "1", "0", "are there notes", "alert", 3, "location", "2020-03-03", "2020-03-10", "10", "" )

    db.close()
    
        
if __name__ == '__main__':
    try:
        db = MySQLdb.connect("sql12.freesqldatabase.com","sql12332583","xy4HDHXWVT","sql12332583")
        c = db.cursor()
    except:
        print ("Can't connect to Server...")
             
    try:
        main()
    except KeyboardInterrupt:
        print ("bye bye...")
        pass    