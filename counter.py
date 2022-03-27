
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    days_dictionary = dict()

    try: 
        file_open = open(file_name)
    except: 
        print('File cannot be opened:', file_name)
        exit()

    for line in file_open: 
        words = line.split() 
        #print(line)
        if line.startswith('From '): 
            if words[2] not in days_dictionary: 
                days_dictionary[words[2]] = 1
            else: 
                days_dictionary[words[2]] += 1 
    print(days_dictionary)

        

countDayOfTheWeek()

# end assignment
## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#countDayOfTheWeek()