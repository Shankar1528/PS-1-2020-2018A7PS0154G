# IO basics

# Printing to the screen
#print("statement")
print "Python is really a great language,", "isn't it?"

# Reading Keyboard Input
# var_name = input("Prompt")

str = input("Enter your input: ")
print "Received input is : ", str

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

# Close opend file
fo.close()
