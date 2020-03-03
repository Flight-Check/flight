# Finding Flights Script
# CREATED BY ADBY IT AND MEDIA SOLUTIONS
# VERSION 1.5
# DATE 6 Jan 2020
# UPDATED 9 Jan 2020
# AUTHOR ADAM R WOLARCZUK


import mysql.connector
import finddatatime  # Getting the date from the second script called finddatetime.py
import time
from mysql.connector import Error
from __main__ import *

currentdatetime = finddatatime.date_time
firstrun = "0"
print('The Current time date is' + ' ' + currentdatetime)



def  dbconnect(fnumber):
    global firstrun

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Ayva@0401',
        database='flightdata'
    )

    mycursor = mydb.cursor()
    print(firstrun)


    sql = 'SELECT * FROM flightdata.flightinfo where flightnumbers =' + "'" + fnumber + "'"
    # print(sql)

    mycursor.execute(sql)
    # connection.commit()

    myresult = mycursor.fetchall()

    for x in myresult:
        flightnumber = x[3]
        orgin = x[10]
        dest = x[2]
        departtime = x[4]
        status = x[8]
        if firstrun == "0":
            firstrun = '1'
            print(firstrun)
            findflight(flightnumber, orgin, dest, departtime, status)
        if firstrun == "1":
            print("i am here")
            getflightupdate(flightnumber, orgin, dest, departtime, status)








def start():
    firstrun = "0"
    fnumber = (input('Please enter flight number:  '))
    dbconnect(fnumber)


def repeat():
    start()
##########THIS WILL END THE SCRIPT###########
def stop():

    print('Thank you for using FLIGHT CHECK!!')
    quit()
##########THIS WILL END THE SCRIPT###########

def getflightupdate(flightnumber, orgin, dest, departtime, status):





    print('Current status of your flight as of ' + currentdatetime + ' is ' + str(status))



def findflight(flightnumber, orgin, dest, departtime, status):
    global firstrun


    answer = (input('Flight #: ' + str(flightnumber) + ' From: ' + str(orgin) + ' To: ' + str(dest) + ' At: ' + str(
        departtime) + 'is that correct? yes/no: '))
    # if statment for answer start



    if answer == 'yes':
        print('Current status of your flight as of ' + currentdatetime + ' is ' + str(status))
        # If statment for reminder start
        remind = (input('Would you like me to remind you of the status of your flight? yes/no: '))
        if remind == 'yes':
            firstrun = 1
            print(firstrun)
            dbconnect(flightnumber)
            print('Loop to check database')
        elif remind == 'no':

            quit()
        # if statment for reminder ends
    elif answer == 'no':
        #answer will be moved to its own script so it can be reused
        firstrun = 0
        start()

        # if statment for answer end


#######APP STARTS#######
start()


