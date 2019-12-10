# Functions on this page gather information about the running status of the deal registration bots
# Information gathered includes the date and time that each vendor bot has run, if at all, on the current date


def auditDell(currentDate):
    exists = False
    content = ''
    # Opens the appropriate event log file for the vendor in the shared file location
    with open('//insight.com/team/RPA/Prod/DealReg.00000/USAZWRPAPBR03.EventLog.txt') as myfile:
        for line in myfile:
            # Searches for the vendor in the event log with an occurrence on the current date
            # If occurrence is found, the latest time occurrence is gather
            if line.find(currentDate) != -1 and line.find('Dell EMC process STARTED') != -1:
                exists = True
                content = line[11:22]
    # If an occurrence for the given date is found a 'True' flag and the time is returned
    if exists == True:
        return 'True', content
    else:
        return 'False'


def auditVMware(currentDate):
    exists = False
    content = ''
    with open('//insight.com/team/RPA/Prod/DealReg.00000/USAZWRPAPBR03.EventLog.txt') as myfile:
        for line in myfile:
            if line.find(currentDate) != -1 and line.find('VMware process STARTED') != -1:
                exists = True
                content = line[11:22]
    if exists == True:
        return 'True', content
    else:
        return 'False'


def auditLenovo(currentDate):
    exists = False
    content = ''
    with open('//insight.com/team/RPA/Prod/DealReg.00000/USAZWRPAPBR05.EventLog.txt') as myfile:
        for line in myfile:
            if line.find(currentDate) != -1 and line.find('Lenovo process STARTED') != -1:
                exists = True
                content = line[11:22]
    if exists == True:
        return 'True', content
    else:
        return 'False'


def auditAPC(currentDate):
    exists = False
    content = ''
    with open('//insight.com/team/RPA/Prod/DealReg.00000/USAZWRPAPBR05.EventLog.txt') as myfile:
        for line in myfile:
            if line.find(currentDate) != -1 and line.find('APC process STARTED') != -1:
                exists = True
                content = line[11:22]
    if exists == True:
        return 'True', content
    else:
        return 'False'


def auditHPE(currentDate):
    exists = False
    content = ''
    with open('//insight.com/team/RPA/Prod/DealReg.00000/USAZWRPAPBR04.EventLog.txt') as myfile:
        for line in myfile:
            if line.find(currentDate) != -1 and line.find('Hewlett Packard Enterprise process STARTED') != -1:
                exists = True
                content = line[11:22]
    if exists == True:
        return 'True', content
    else:
        return 'False'


def auditHPI(currentDate):
    exists = False
    content = ''
    with open('//insight.com/team/RPA/Prod/DealReg.00000/USAZWRPAPBR04.EventLog.txt') as myfile:
        for line in myfile:
            if line.find(currentDate) != -1 and line.find('HPI process STARTED') != -1:
                exists = True
                content = line[11:22]
    if exists == True:
        return 'True', content
    else:
        return 'False'