import cowsay

import mymodule #Real name of the module
import mymodule as md # Using alias for the module
import platform # Used for system info
from mymodule import person1


# Greeting a person
mymodule.greeting("Tarun")

# Printing a dictionary 
a = md.person1
print(a)

# Returns the system name
x = platform.system()
print(x)

# Returns the directory present in the system
x=dir(platform)
print(x)

# printing the age of person1 from mymodule
print(person1['age'])

print(dir(mymodule))

print(cowsay.cow("Good Mooooooooring!"))