## Python program to illustrate 
## the use of timedelta class
from datetime import datetime, timedelta  
    
presentdate = datetime.now()  
print ("Present date:", str(presentdate))  
    
## Date and time after 4 years
date1 = presentdate + timedelta(days = (4*365))  
print ("Date after 4 years from now", str(date1))  
    
# Date and time after 4 years 2 months 3 hours from now  
date2 = presentdate + timedelta(days = (4*365+2*30), hours=3)   
print ("Date after 4 years 2 months 3 hours from now", str(date2))

## total_seconds function
total = timedelta(minutes = 2*15).total_seconds()
print("Total seconds in 30 minutes:", total)
