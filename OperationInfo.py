from datetime import date
import datetime

today = date.today()
currentDay = today.day
currentMonth = today.month
currentYear = today.year
currentDate = str(currentMonth) + '/' + str(currentDay) + "/" + str(currentYear)

def occurrenceTime(occurrence):
    lastOccurrence = occurrence.split(':')
    if lastOccurrence[2].find('P') != -1:
        if int(lastOccurrence[0]) >= 8 and int(lastOccurrence[0]) != 12:
            lastOccurrenceHour = int(lastOccurrence[0]) - 7
            lastOccurrenceCycle = 'PM'
        elif int(lastOccurrence[0]) == 7:
            lastOccurrenceHour = 12
            lastOccurrenceCycle = 'PM'
        elif int(lastOccurrence[0]) <= 6:
            if int(lastOccurrence[0]) == 6:
                lastOccurrenceHour = 11
            if int(lastOccurrence[0]) == 5:
                lastOccurrenceHour = 10
            if int(lastOccurrence[0]) == 4:
                lastOccurrenceHour = 9
            if int(lastOccurrence[0]) == 3:
                lastOccurrenceHour = 8
            if int(lastOccurrence[0]) == 2:
                lastOccurrenceHour = 7
            if int(lastOccurrence[0]) == 1:
                lastOccurrenceHour = 6
            lastOccurrenceCycle = 'AM'
        else:
            lastOccurrenceHour = 5
            lastOccurrenceCycle = 'AM'

    else:
        if int(lastOccurrence[0]) >= 8 and int(lastOccurrence[0]) != 12:
            lastOccurrenceHour = int(lastOccurrence[0]) - 7
            lastOccurrenceCycle = 'AM'
        elif int(lastOccurrence[0]) == 7:
            lastOccurrenceHour = 12
            lastOccurrenceCycle = 'AM'
        elif int(lastOccurrence[0]) <= 6:
            if int(lastOccurrence[0]) == 6:
                lastOccurrenceHour = 11
            if int(lastOccurrence[0]) == 5:
                lastOccurrenceHour = 10
            if int(lastOccurrence[0]) == 4:
                lastOccurrenceHour = 9
            if int(lastOccurrence[0]) == 3:
                lastOccurrenceHour = 8
            if int(lastOccurrence[0]) == 2:
                lastOccurrenceHour = 7
            if int(lastOccurrence[0]) == 1:
                lastOccurrenceHour = 6
            lastOccurrenceCycle = 'PM'
        else:
            lastOccurrenceHour = 5
            lastOccurrenceCycle = 'PM'
    lastOccurrenceMinute = lastOccurrence[1]
    return "{}:{} {}".format(lastOccurrenceHour, lastOccurrenceMinute, lastOccurrenceCycle)

def isRunning(time):
    ref = time
    time = time[:-2]
    timeSub = time.split(':')
    now = datetime.datetime.now()
    nowHour = now.hour
    nowMin = now.minute
    x = int(timeSub[0])
    y = int(timeSub[1])
    if ref.find('PM') != -1 and x != 12:
        x = x + 12
    difHour = nowHour - x
    difMin = nowMin - y
    if difHour != 0 and difHour != 1 and difHour != -23:
        return 'No'
    else:
        if difMin <= 0:
            if -59 <= difMin <= -40 or difMin == 0:
                return 'Yes'
            else:
                return 'No'
        else:
            a = difMin
            if a > 20:
                return 'No'
            else:
                return 'Yes'


