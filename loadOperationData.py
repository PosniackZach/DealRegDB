# Functions on this page take the information from AuditData and OperationInfo to load into SQLite database
# Table in SQLite database is called 'audit'


import sqlite3
from sqlite3 import Error
from AuditData import auditDell, auditVMware, auditLenovo, auditAPC, auditHPE, auditHPI
from OperationInfo import occurrenceTime, isRunning, currentDate


# Creates Connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\ZPOSNIAC\PycharmProjects\DealRegDash\DealRegDB\dealreg.db")
    except Error:
        print(Error)

    return conn


# Updated the 'audit' table with audit data information
# Function will also create the 'audit' table if it doesn't already exist
def update_tablevalues(content, conn):
    cur = conn.cursor()
    cur.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='audit' ''')
    if cur.fetchone()[0] != 1:
        create = ''' CREATE TABLE IF NOT EXISTS audit (
                    vendor TEXT PRIMARY KEY,
                    running TEXT,
                    lastrun TEXT
                            ); '''
        cur.execute(create)
        vendors = ['Dell', 'VMware', 'Lenovo', 'APC', 'HPE', 'HPI']
        for x in vendors:
            var = (x, 'Null', 'Null')
            insert = ''' INSERT INTO audit(vendor,running,lastrun)
                          VALUES(?,?,?) '''
            cur.execute(insert, var)
    sql = ''' UPDATE audit
                 SET running = ? ,
                     lastrun = ?
                 WHERE vendor = ? '''
    cur.execute(sql, content)
    conn.commit()


# This is the main function on this page
# The function will grab data from AuditData, process the information through functions in OperationInfo, and post
# the result in the 'audit' table
def load_OperationData():
    vendors = ['Dell', 'VMware', 'Lenovo', 'APC', 'HPE', 'HPI']
    for x in vendors:
        if x == 'Dell':
            try:
                result, occurrence = auditDell(currentDate)
                lastOccurrence = occurrenceTime(occurrence)
            except:
                result = 'No'
                lastOccurrence = 'Null'
        elif x == 'VMware':
            try:
                result, occurrence = auditVMware(currentDate)
                lastOccurrence = occurrenceTime(occurrence)
            except:
                result = 'No'
                lastOccurrence = 'Null'
        elif x == 'Lenovo':
            try:
                result, occurrence = auditLenovo(currentDate)
                lastOccurrence = occurrenceTime(occurrence)
            except:
                result = 'No'
                lastOccurrence = 'Null'
        elif x == 'APC':
            try:
                result, occurrence = auditAPC(currentDate)
                lastOccurrence = occurrenceTime(occurrence)
            except:
                result = 'No'
                lastOccurrence = 'Null'
        elif x == 'HPE':
            try:
                result, occurrence = auditHPE(currentDate)
                lastOccurrence = occurrenceTime(occurrence)
            except:
                result = 'No'
                lastOccurrence = 'Null'
        elif x == 'HPI':
            try:
                result, occurrence = auditHPI(currentDate)
                lastOccurrence = occurrenceTime(occurrence)
            except:
                result = 'No'
                lastOccurrence = 'Null'
        else:
            print("This vendor is currently not supported")
            break
        if result == 'True':
            result = isRunning(lastOccurrence)
        conn = create_connection()
        update_tablevalues((result, lastOccurrence, x), conn)
