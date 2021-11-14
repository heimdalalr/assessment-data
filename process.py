log_file = open("um-server-01.txt") #the variable log-file opens the parameter of um-server01.txt as readable, because the default is to read the text you do not have to declare the the file modes


def sales_reports(log_file): #define function sales_reports from the argument log_file
    for line in log_file: #loops the file define in log_file
        line = line.rstrip() # returns the copy of the string by removing the trailing characters specified 
        day = line[0:3] #day is defined on each line as the first 3 characters
        if day == "Mon": #if the day is Monday
            print(line) #print the line


sales_reports(log_file)
#log_file.close() #it is best practice to close the file when you are done with it