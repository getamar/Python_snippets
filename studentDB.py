#Write a program to get input from user

student_db = []

def getLoad():
    if len(split_st) > 1:
        DB_FileName = split_st[1]
    else:
        DB_FileName = "studentDbLoadFile.csv"
    DB_READ_FH = open(DB_FileName, 'a+')
    DB_LIST = DB_READ_FH.read().split("\n")
    for i in range(0,len(DB_LIST)):
        if str(DB_LIST[i]).split(";") != ['']:
            student_db.append(str(DB_LIST[i]).split(";"))
        else:
            continue
    DB_READ_FH.close()
    return

def getExit():
    exit()

def getNew():
    s3 = [split_st[1],split_st[2],split_st[3]]
    student_db.append(s3)

def getAverage():
    counter = 1
    sum = 0.0
    for _ in range(1, len(student_db)):
        sum = sum + int(student_db[counter][1])
        counter = counter + 1
    print sum/counter

def getPrint():
    counter = 1
    if len(student_db) > 0:
        print "There are %s records in the database without header\n" %(len(student_db)-1)
    else:
        print"Nothing to print now\n"
    if len(student_db) > 1:
        for i in range(1, len(student_db)):
            print "%s is %s year experienced and work as %s\n" % (student_db[counter][0], student_db[counter][1], student_db[counter][2])
            counter = counter + 1
    return

def getSave():
    DB_FileName = "studentDbFile_out.csv"
    DB_OUT = open(DB_FileName, 'w+')
    DB_OUT.write("StudentName;Exp;Occupation\n")
    counter = 1
    if len(student_db) > 1:
        DB_OUT.write("Student Name;Exp;Occupation\n")
        for i in range(1, len(student_db)):
            DB_OUT.write("%s;%s;%s\n" % (student_db[counter][0], student_db[counter][1], student_db[counter][2]))
            counter += 1
    DB_OUT.close()
    getPrint()

def getSavecsv():
    return

def getLoadcsv():
    return

while (True):

    print "you have following options"
    print "1. New - eg. New J 20 Music\n" \
          "2. Print - eg. print \n" \
          "3. Average - eg. average or avg\n" \
          "4. Save - Saved file is studentDbFile_out.csv \n" \
          "5. Load - Header required for first load alone\n" \
          "6. Exit\n"
    raw_st = raw_input("please choose your option\n")
    split_st = raw_st.split(' ')
    command = split_st[0]

    if command.lower() == 'exit':
        getExit()
    elif command.lower() == 'print':
        getPrint()
    elif command.lower() == 'new':
        getNew()
    elif command.lower() == 'average' or command.lower() == 'avg':
        getAverage()
    elif command.lower() == 'save':
        getSave()
    elif command.lower() == 'load':
        getLoad()
    elif command.lower() == 'savecsv':
        getSavecsv()
    elif command.lower() == 'loadcsv':
        getLoadcsv()
    else:
        continue

    redundant = raw_input("Actions done? If so hit enter to continue\t")