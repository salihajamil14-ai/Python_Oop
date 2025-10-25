# Python Object Oriented Programming: Classes and Instances


# Making a Class

class Employee:
    pass

emp_1 = Employee() # Creating an instance of the Employee class
emp_2 = Employee() # Creating another instance of the Employee class

print(emp_1)
print(emp_2)

emp_1.first = "John"  # Adding attributes to the emp_1 instance
emp_1.last = "Doe" # Adding attributes to the emp_1 instance
emp_1.email = 'john.doe@email.com' # Adding attributes to the emp_1 instance
emp_1.pay = 50000 # Adding attributes to the emp_1 instance

emp_2.first = "Jane" # Adding attributes to the emp_2 instance
emp_2.last = "Smith" # Adding attributes to the emp_2 instance
emp_2.email = 'jane.smith@email.com' # Adding attributes to the emp_2 instance
emp_2.pay = 60000 # Adding attributes to the emp_2 instance

print(emp_1.email)
print(emp_2.email)


# Using the __init__ Method
class Employee:
    def __init__(self, first, last, pay):
        self.first = first # Adding attributes to the instance
        self.last = last # Adding attributes to the instance
        self.email = first + '.' + last + '@email.com' # Adding attributes to the instance
        self.pay = pay  # Adding attributes to the instance

emp_1 = Employee('John', 'Doe', 50000) # Creating an instance of the Employee class
emp_2 = Employee('Jane', 'Smith', 60000) # Creating another instance of the Employee class

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))



# Adding Methods to a Class
class Employee:
    def __init__(self, first, last, pay):
        self.first = first # Adding attributes to the instance
        self.last = last # Adding attributes to the instance
        self.email = first + '.' + last + '@email.com' # Adding attributes to the instance
        self.pay = pay  # Adding attributes to the instance
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last) # Method to return full name of the employee

emp_1 = Employee('John', 'Doe', 50000) # Creating an instance of the Employee class
emp_2 = Employee('Jane', 'Smith', 60000) # Creating another instance of the Employee class

# print(emp_1)
# print(emp_2)

# Calling methods
emp_1.fullname() # Calling the fullname method for emp_1
emp_2.fullname() # Calling the fullname method for emp_2

# Using the fullname method from the class
print(Employee.fullname(emp_1)) # Calling the fullname method using the class name
print(Employee.fullname(emp_2)) # Calling the fullname method using the class name

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) # Calling the fullname method for emp_1
print(emp_2.fullname()) # Calling the fullname method for emp_2