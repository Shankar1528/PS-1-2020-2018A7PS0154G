# Python program to display calendar of  
# given month of the year  
    
# import module  
import calendar  
    
yy = 2017
mm = 11
    
# display the calendar  
print(calendar.month(yy, mm))  

# using calender to print calendar of year  
# prints calendar of 2018  
print ("The calender of year 2018 is : ")  
print (calendar.calendar(2018, 2, 1, 6)) 
