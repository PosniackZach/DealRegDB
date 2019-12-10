# Functions on this page gather information about the errors for each deal registration bot
# Information gathered includes the vendor, the error line number, and the amount of occurrences for each error


def errorDell():
    # Opens the error log file in the shared file location
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        # Finds the beginning of every error message for the given vendor and grabs the error line number
        # Line error is added to a list of all of the errors found for the vendor
        for line in myfile:
            if line.find('Dell EMC ERROR') != -1:
                x = count + 3
                errors.append(lines[x])
            count += 1
        # Error list is cleaned
        for z in range(len(errors)):
            errors[z] = errors[z].strip('\n')
        errorsDup = list(dict.fromkeys(errors))
        botError = []
        for a in range(len(errorsDup)):
            if errorsDup[a].find('BotRunner') != -1:
                botError.append(a)
        # Error list is ran to count for occurrences and a separate list of occurrences is made
        botError.reverse()
        for b in range(len(botError)):
            del errorsDup[botError[b]]
        occurrences = []
        for i in range(len(errorsDup)):
            curVal = errorsDup[i]
            occurrence = 0
            for j in range(len(errors)):
                newVal = errors[j]
                if curVal == newVal:
                    occurrence += 1
            occurrences.append(occurrence)
        # Returns the list of errors as well as the list of occurrences
        return errorsDup, occurrences


def errorVMware():
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        for line in myfile:
            if line.find('VMware ERROR') != -1:
                x = count + 3
                errors.append(lines[x])
            count += 1
        for z in range(len(errors)):
            errors[z] = errors[z].strip('\n')
        errorsDup = list(dict.fromkeys(errors))
        botError = []
        for a in range(len(errorsDup)):
            if errorsDup[a].find('BotRunner') != -1:
                botError.append(a)
        botError.reverse()
        for b in range(len(botError)):
            del errorsDup[botError[b]]
        occurrences = []
        for i in range(len(errorsDup)):
            curVal = errorsDup[i]
            occurrence = 0
            for j in range(len(errors)):
                newVal = errors[j]
                if curVal == newVal:
                    occurrence += 1
            occurrences.append(occurrence)
        return errorsDup, occurrences


def errorLenovo():
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        for line in myfile:
            if line.find('Lenovo ERROR') != -1:
                x = count + 3
                errors.append(lines[x])
            count += 1
        for z in range(len(errors)):
            errors[z] = errors[z].strip('\n')
        errorsDup = list(dict.fromkeys(errors))
        botError = []
        for a in range(len(errorsDup)):
            if errorsDup[a].find('BotRunner') != -1:
                botError.append(a)
        botError.reverse()
        for b in range(len(botError)):
            del errorsDup[botError[b]]
        occurrences = []
        for i in range(len(errorsDup)):
            curVal = errorsDup[i]
            occurrence = 0
            for j in range(len(errors)):
                newVal = errors[j]
                if curVal == newVal:
                    occurrence += 1
            occurrences.append(occurrence)
        return errorsDup, occurrences


def errorAPC():
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        for line in myfile:
            if line.find('APC ERROR') != -1:
                x = count + 3
                errors.append(lines[x])
            count += 1
        for z in range(len(errors)):
            errors[z] = errors[z].strip('\n')
        errorsDup = list(dict.fromkeys(errors))
        botError = []
        for a in range(len(errorsDup)):
            if errorsDup[a].find('BotRunner') != -1:
                botError.append(a)
        botError.reverse()
        for b in range(len(botError)):
            del errorsDup[botError[b]]
        occurrences = []
        for i in range(len(errorsDup)):
            curVal = errorsDup[i]
            occurrence = 0
            for j in range(len(errors)):
                newVal = errors[j]
                if curVal == newVal:
                    occurrence += 1
            occurrences.append(occurrence)
        return errorsDup, occurrences


def errorHPE():
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        for line in myfile:
            if line.find('Hewlett Packard Enterprise ERROR') != -1:
                x = count + 3
                errors.append(lines[x])
            count += 1
        for z in range(len(errors)):
            errors[z] = errors[z].strip('\n')
        errorsDup = list(dict.fromkeys(errors))
        botError = []
        for a in range(len(errorsDup)):
            if errorsDup[a].find('BotRunner') != -1:
                botError.append(a)
        botError.reverse()
        for b in range(len(botError)):
            del errorsDup[botError[b]]
        occurrences = []
        for i in range(len(errorsDup)):
            curVal = errorsDup[i]
            occurrence = 0
            for j in range(len(errors)):
                newVal = errors[j]
                if curVal == newVal:
                    occurrence += 1
            occurrences.append(occurrence)
        return errorsDup, occurrences


def errorHPI():
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        for line in myfile:
            if line.find('HPI ERROR') != -1:
                x = count + 3
                errors.append(lines[x])
            count += 1
        for z in range(len(errors)):
            errors[z] = errors[z].strip('\n')
        errorsDup = list(dict.fromkeys(errors))
        botError = []
        for a in range(len(errorsDup)):
            if errorsDup[a].find('BotRunner') != -1:
                botError.append(a)
        botError.reverse()
        for b in range(len(botError)):
            del errorsDup[botError[b]]
        occurrences = []
        for i in range(len(errorsDup)):
            curVal = errorsDup[i]
            occurrence = 0
            for j in range(len(errors)):
                newVal = errors[j]
                if curVal == newVal:
                    occurrence += 1
            occurrences.append(occurrence)
        return errorsDup, occurrences