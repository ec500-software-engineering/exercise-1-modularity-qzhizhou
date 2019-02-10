fileName = "input.txt"

file = open(fileName, "r")
fileContent = file.read().splitlines()
fileContent = [i.split() for i in fileContent]


#error check function
def ErrorCheck(line):
    checkEx1 = ["ID", "NAME", "GENDER", "AGE"]
    checkEx2 = ["ID", "PULSE", "PULSE RANGE", "BLOOD PRESSURE", "PRESSURE RANGE", "BLOOD OXYGEN", "OXYGEN RANGE", "TIME"]
    p = True
    
    if len(line) == len(checkEx1):
        for n, i in enumerate(line):
            if i == "null":
                print(checkEx1[n] + " IS MISSING")
                p = False

        return p

    elif len(line) == len(checkEx2):
        for n, i in enumerate(line):
            if i == "null":
                print(checkEx2[n] + " IS MISSING")
                p = False
                
        return p


# output data
for line in fileContent:
    if ErrorCheck(line):
        if len(line) == 4:
            data1 = {}   
            data1[line[0]] = {'name': line[1],
                              'gender': line[2],
                              'age': line[3]}
            print(data1)
        elif len(line) == 8:
            lower2, upper2 = line[2].split("-")
            lower4, upper4 = line[4].split("-")
            lower6, upper6 = line[6].split("-")
            data2 = {}
            data2[line[0]] = {'pulse': line[1],
                              'pulseRange': {'lower': lower2, 'upper': upper2},
                              'bloodPressure': line[3],
                              'pressureRange': {'lower':lower4, 'upper':upper4},
                              'bloodOx': line[5],
                              'oxRange': {'lower':lower6, 'upper':upper6},
                              'time': line[7]}
            print(data2)

    

