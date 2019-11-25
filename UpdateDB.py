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
        print('Load Success')
    except:
        print('Load Fail')
    time.sleep(delay)
