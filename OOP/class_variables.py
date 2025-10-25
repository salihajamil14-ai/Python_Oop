# Class Variables

# Making a Class
class Employee:
    
    # Class variable to keep track of number of employees
    num_of_emps = 0
    raise_amount = 1.04 # Class variable for raise amount
    
    def __init__(self, first, last, pay): # Constructor method
        self.first = first # Instance variable for first name
        self.last = last # Instance variable for last name
        self.email = first + '.' + last + '@company.com' # Instance variable for email
        self.pay = pay  # Instance variable for pay

        Employee.num_of_emps += 1 # Incrementing the number of employees

    def fullname(self): # Method to return full name of the employee
        return '{} {}'.format(self.first, self.last) # Method to return full name of the employee

    def apply_raise(self): # Method to apply raise to the employee's pay
        self.pay = int(self.pay * self.raise_amount) # Applying raise to the employee's pay

print(Employee.num_of_emps) # Accessing class variable before creating any instances

emp_1 = Employee('John', 'Doe', 50000) # Creating an instance of the Employee class
emp_2 = Employee('Jane', 'Smith', 60000) # Creating another instance of the Employee class

print(Employee.num_of_emps)

# print(emp_1.__dict__)
# print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05 # Changing the raise amount for all instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06 # Changing the raise amount for emp_1 instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Applying raise using class variable
print(Employee.num_of_emps) # Accessing class variable

print(emp_1.__dict__)
