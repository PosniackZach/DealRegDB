# This is the main page of this project
# This page prompts the user for run and refresh times and runs the functions that update the SQLite tables


import time
from loadOperationData import load_OperationData
from loadErrorData import load_ErrorData
from ErrorTable import error_table

runtime = int(input("How long would you like to run this automation? hour(s) "))
refresh = int(input("How often would you like to refresh your data? minute(s) "))
delay = refresh * 60
runPerHour = (60/refresh) + 1
runTotal = runPerHour * runtime
while runTotal > 0:
    try:
        load_OperationData()
        load_ErrorData()
        error_table()
    except:
        print('Load Fail')
    time.sleep(delay)
    runTotal -= 1
    if runTotal == 1:
        print('This is the final update')
