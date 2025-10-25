# Import Modules and Exploring The Standard Library

# importing the entire module
import my_module_import as mm 
# importing specific functions from a module
from my_module_import import find_index, test

from my_module_import import * # imports everything from the module
import sys # to explore module search path

# sys.path.append('C:\\Users\\aliwa\\Downloads\\Python_oop\\Basics') # adding a new path to search modules

import math as ma  # importing the math module with an alias
import datetime  # importing the datetime module
import calendar  # importing the calendar module
import os  # importing the os module

# Using the imported functions and variables
courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print(index)  # Output: 1

index = find_index(courses, 'Math') # Using imported function directly
print(index)  # Output: 1
print(test)  # Output: This is a test string from import_modules.py

print(sys.path)  # Output: List of directories Python searches for modules

import random  # Importing the random module

random_course = random.choice(courses)  # Using a function from the random module
print(random_course)  # Output: Randomly selected course from the list

rads = ma.radians(90)  # Converting degrees to radians using math module
print(rads)  # Output: 1.5707963267948966
print(ma.sin(rads))  # Calculating sine of 90 degrees (in radians) output: 1.0

print(datetime.date.today())  # Output: Current date
print(calendar.isleap(2024))  # Output: True (2024 is a leap year)

print(os.getcwd())  # Output: Current working directory
print(os.__file__)  # Output: Path to the os module file

import  antigravity  # Fun Easter egg module in Python

