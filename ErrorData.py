def errorDell():
    with open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt') as myfile:
        lines = open('//insight.com/team/RPA/Prod/DealReg.00000/ErrorLog.txt').readlines()
        errors = []
        count = 0
        for line in myfile:
            if line.find('Dell EMC ERROR') != -1:
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