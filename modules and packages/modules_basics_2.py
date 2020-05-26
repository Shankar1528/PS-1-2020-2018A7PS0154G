# Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name) 
  
  import mymodule

mymodule.greeting("Jonathan")

# Renaming a module
import mymodule as mx

a = mx.person1["age"]
print(a) 

#Built in module
import platform

x = platform.system()
print(x) 

# Using the dir() Function
import platform

x = dir(platform)
print(x) 

# Import From Module
# The module named mymodule has one function and one dictionary
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import only the person1 dictionary from the module

from mymodule import person1

print (person1["age"])
