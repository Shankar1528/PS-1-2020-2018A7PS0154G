import numpy as np 
a = np.array([1,2,3,4]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying average() function:' 
print np.average(a) 
print '\n'  

# this is same as mean when weight is not specified 
wts = np.array([4,3,2,1]) 

print 'Applying average() function again:' 
print np.average(a,weights = wts) 
print '\n'  

# Returns the sum of weights, if the returned parameter is set to True. 
print 'Sum of weights' 
print np.average([1,2,3, 4],weights = [4,3,2,1], returned = True)
