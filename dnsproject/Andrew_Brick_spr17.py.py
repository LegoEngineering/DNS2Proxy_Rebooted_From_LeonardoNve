#ANDREW BRICK
#DNSPROJECT (undergraduate part)- ECE580F


import string
import re
input = open("dnslog.txt", "r")
output = open("report.txt","w")

def Task_1():
    
    j = 0
    connection_log = []
    request = []
    hosts = []
    last_hostname = ""
    visit_count = 0
    timestamp = []
    time = []
    time_range = 0
    delta_t = 0
    output_time = ""
    
	#collect all of the middle-handshake transactions into a list. This is a list of singular connections. 
    for line in input:
      for i in range(len(line)):
        if line[i:i+4] == "AAAA": #AAAA arrives only once during the connection, making it a good indicator
          connection_log.append(line) #create a list of connections
          timestamp.append(line[11:24]) #create a list  of timestamps
          
	#convert timestamps into millisecond values
    for i in range(len(timestamp)):
      timestamp_elements = timestamp[i].split(":") #the units of time are divided by colons
      hours = long(timestamp_elements[0]) * 3600000
      minutes = long(timestamp_elements[1]) * 60000
      second_section = timestamp_elements[2].split(".") #divide seconds from milliseconds
      seconds = long(second_section[0]) * 1000
      milliseconds = long(second_section[1])
      time.append(hours + minutes + seconds + milliseconds) #combine the times and add them to a list of times
      
	#determine if the request was fulfilled within a small period of time from the host connection
    for line in connection_log:
      delta_t = abs(time_range - time[j]) #determine the difference in time from the connection
      if line[62:65] != 'www' and delta_t >= 59650: #if the difference in time is greater than just under a minute, and is not the name of the host...
 	hosts.append(line)       
	time_range = time [j] #reassign the time range to be for the next connection
      j += 1
      
	#count the number of visits to a host
    for line in connection_log:
      for host in hosts:
        if host == line: #if the connection was also to the host...
          if visit_count != 0: #and the site has already been shown to be visited
            writeout_first(request,visit_count,output_time)
            writeout(j,i,request)
	  visit_count = 0
          request = [] #clear the list of requests
	  last_hostname = host
      if visit_count == 0: #if the site has never been visited...
         output_time = line[0:23]
      visit_count += 1 #increment the visit count
      #isolate and collect the URL text
      URL = ""
      URL_start = True
      URL_copy = False
      URL_end = False
      for i in range(len(line)): #read through the characters in each connection
        if URL_copy == True and line[i:i+2] == ". ": #if it is the end of the URL...
	  URL_start = False #signal it is not the opening to the URL
          URL_copy = False #signal to stop recording the characters 
        if URL_copy == True: #if it is the proper place in the line to record the URL...
          URL = URL + line[i] #record the characters into the URL
        if URL_start == True and line[i:i+5] == "s    ": #if it is the opening of the URL...
          URL_copy = True #signal to record the characters
        if URL_start == False and line[i:i+5] == "s    ": #if it is the opening of the URL...
          URL_end = True #it must be the end of the URL
        if URL_end == True and line[i:i+2] == ". ": #if it is the end of the URL...
          URL_start = True #signal it is the opening to the URL
          URL_end = False #it cannot be the end of the URL
      URL = URL[4:] #omit first four characters
      request.append(URL) #add the URL to the list
    writeout_first(request,visit_count,output_time)
    writeout(j,i,request)

def writeout_first(request,visit_count,output_time):
    output.write(request[0]) 
    output.write(": %d Time: " % visit_count)
    output.write(output_time)
    output.write("\n")

def writeout(j,i,request):
    for i in range(len(request)): 
        j = i + 1
    	output.write("%d. " % j) #number the list
    	output.write(request[i]) #list domain requests
    	output.write("\n")

Task_1()
