# Functions on this page create a table of errors in SQlite database
# This is to replace the 'LoadErrorData' functions for a better alternative on the website side


import sqlite3
from sqlite3 import Error


# Creates Connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\ZPOSNIAC\PycharmProjects\DealRegDash\DealRegDB\dealreg.db")
    except Error:
        print(Error)

    return conn


# Creates the table 'errorTable' if it does not already exists
# Clears all entries so a refresh of error information is done
def prep_table(conn):
    create = ''' CREATE TABLE IF NOT EXISTS errorTable (
                    vendor TEXT,
                    error TEXT,
                    id INT
                            ); '''
    delete = ''' DELETE FROM errorTable '''
    cur = conn.cursor()
    cur.execute(create)
    cur.execute(delete)
    conn.commit()


# Inserts error information into the 'errorTable'
def update_table(vendor, error, request, conn):
    cur = conn.cursor()
    insert = ''' INSERT INTO errorTable(vendor,error,id)
                  VALUES(?,?,?) '''
    var = (vendor, error, request)
    cur.execute(insert, var)
    conn.commit()


# This is the main function
# Loads error data from error logs and uploads it to 'errorTable'
def error_table():
    conn = create_connection()
    prep_table(conn)
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        count = 0
        for line in myfile:
            x = count + 3
            y = count + 1
            if line.find('Dell EMC ERROR') != -1:
                vendor = 'Dell'
            elif line.find('VMware ERROR') != -1:
                vendor = 'VMware'
            elif line.find('Lenovo ERROR') != -1:
                vendor = 'Lenovo'
            elif line.find('APC ERROR') != -1:
                vendor = 'APC'
            elif line.find('Hewlett Packard Enterprise ERROR') != -1:
                vendor = 'HPE'
            elif line.find('HPI ERROR') != -1:
                vendor = 'HPI'
            else:
                count += 1
                continue
            request = lines[y]
            error = lines[x]
            request = request.strip('\n')
            request = request[12:]
            error = error.strip('\n')
            if error.find('BotRunner') != -1:
                count += 1
                continue
            update_table(vendor, error, request, conn)
            count += 1