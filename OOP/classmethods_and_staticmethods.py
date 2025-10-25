# Class Methods and Static Methods

# Making a Class with Class Method
class Employee:
    num_of_emps = 0
    raise_amount = 1.04 # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount # Setting class variable using class method

    
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# Using Class Method to Modify Class Variable
class Employee:
    num_of_emps = 0
    raise_amount = 1.04 # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount # Setting class variable using class method

    
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

Employee.set_raise_amount(1.05) # Using class method to set raise amount
emp_1.set_raise_amount(1.06) # Using class method to set raise amount


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# Alternative Constructor using Class Method
class Employee:
    num_of_emps = 0
    raise_amount = 1.04 # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount # Setting class variable using class method

    
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

emp_str_1 = 'Alice-Wonderland-70000'
emp_str_2 = 'Bob-Builder-80000'
emp_str_3 = 'Charlie-Brown-90000'

first, last, pay = emp_str_1.split('-') # Splitting the string to get first, last and pay
new_emp_1 = Employee(first, last, int(pay)) # Creating a new Employee instance

print(new_emp_1.email)
print(new_emp_1.pay)


# Alternative Constructor using Class Method
class Employee:
    num_of_emps = 0
    raise_amount = 1.04 # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount # Setting class variable using class method

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') # Splitting the string to get first, last and pay
        return cls(first, last, int(pay)) # Returning a new instance of Employee
    
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

emp_str_1 = 'Alice-Wonderland-70000'
emp_str_2 = 'Bob-Builder-80000'
emp_str_3 = 'Charlie-Brown-90000'

first, last, pay = emp_str_1.split('-') # Splitting the string to get first, last and pay
new_emp_1 = Employee.from_string(emp_str_1) # Creating a new Employee instance

print(new_emp_1.email)
print(new_emp_1.pay)



class Employee:
    num_of_emps = 0
    raise_amount = 1.04 # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Class method decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount # Setting class variable using class method

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') # Splitting the string to get first, last and pay
        return cls(first, last, int(pay)) # Returning a new instance of Employee
    
    @staticmethod # Static method decorator
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

import datetime
my_date = datetime.date(2024, 6, 15) # A sample date (Saturday)
print(Employee.is_workday(my_date)) # Using static method to check if it's a workday






