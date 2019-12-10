# Functions on this page take the error data from ErrorData and load it into the SQLite table 'errors'

import sqlite3
from sqlite3 import Error
from ErrorData import errorDell, errorVMware, errorLenovo, errorAPC, errorHPE, errorHPI


# Creates Connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\ZPOSNIAC\PycharmProjects\DealRegDash\DealRegDB\dealreg.db")
    except Error:
        print(Error)

    return conn


# Creates the table 'errors' if it does not already exists
# Clears all entries so a refresh of error information is done
def prep_table(conn):
    create = ''' CREATE TABLE IF NOT EXISTS errors (
                    vendor TEXT,
                    error TEXT,
                    occurrences INT
                            ); '''
    delete = ''' DELETE FROM errors '''
    cur = conn.cursor()
    cur.execute(create)
    cur.execute(delete)
    conn.commit()


# Inserts error information into the 'errors' table
def update_table(vendor, errors, occurrences, conn):
    cur = conn.cursor()
    insert = ''' INSERT INTO errors(vendor,error,occurrences)
                  VALUES(?,?,?) '''
    x = 0
    for error in errors:
        var = (vendor, errors[x], occurrences[x])
        cur.execute(insert, var)
        conn.commit()
        x += 1


# This is the main function
# Loads error data from ErrorData and uploads it to 'errors' table
def load_ErrorData():
    vendors = ['Dell', 'VMware', 'Lenovo', 'APC', 'HPE', 'HPI']
    conn = create_connection()
    prep_table(conn)
    for x in vendors:
        conn = create_connection()
        if x == 'Dell':
            errors, occurrences = errorDell()
        elif x == 'VMware':
            errors, occurrences = errorVMware()
        elif x == 'Lenovo':
            errors, occurrences = errorLenovo()
        elif x == 'APC':
            errors, occurrences = errorAPC()
        elif x == 'HPE':
            errors, occurrences = errorHPE()
        elif x == 'HPI':
            errors, occurrences = errorHPI()
        else:
            print("This vendor is currently not supported")
            break
        update_table(x, errors, occurrences, conn)
