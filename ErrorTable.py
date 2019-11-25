import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\ZPOSNIAC\PycharmProjects\DealRegDash\DealRegDB\dealreg.db")
    except Error:
        print(Error)

    return conn

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

def update_table(vendor, error, request, conn):
    cur = conn.cursor()
    insert = ''' INSERT INTO errorTable(vendor,error,id)
                  VALUES(?,?,?) '''
    var = (vendor, error, request)
    cur.execute(insert, var)
    conn.commit()

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