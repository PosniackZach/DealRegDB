import sqlite3
from sqlite3 import Error
from ErrorData import errorDell, errorVMware, errorLenovo, errorAPC, errorHPE, errorHPI

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"C:\Users\ZPOSNIAC\PycharmProjects\DealRegDash\DealRegDB\dealreg.db")
    except Error:
        print(Error)

    return conn

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
