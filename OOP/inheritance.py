# Inheritance in Python

## Creating a Base Class
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
## Creating a Derived Class    
class Developer(Employee):  # Inheriting from Employee class
    pass

dev_1 = Employee('John', 'Doe', 50000)
dev_2 = Employee('Jane', 'Smith', 60000)

# dev_1 = Developer('John', 'Doe', 50000) # Creating an instance of the Developer class
# dev_2 = Developer('Jane', 'Smith', 60000) # Creating another instance of the Developer class

# print(help(Developer))  # Displaying the method resolution order for Developer class

print(dev_1.email)
print(dev_2.email)

# Using Inherited Method
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
## Creating a Derived Class    
class Developer(Employee):  # Inheriting from Employee class
    pass

dev_1 = Employee('John', 'Doe', 50000)
dev_2 = Employee('Jane', 'Smith', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Overriding Attributes and Methods in Derived Class
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
## Creating a Derived Class    
class Developer(Employee):  # Inheriting from Employee class
    raise_amount = 1.10  # Overriding class variable for raise amount
    def __init__(self, first, last, pay, prog_lang): # Constructor method
        super().__init__(first, last, pay)  # Calling the constructor of the base class
        self.prog_lang = prog_lang  # Adding new instance variable for programming language
        
dev_1 = Developer('John', 'Doe', 50000, 'Python') # Creating an instance of the Developer class
dev_2 = Developer('Jane', 'Smith', 60000, 'Java') # Creating another instance of the Developer class

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


# Extending Functionality in Derived Class
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
## Creating a Derived Class    
class Developer(Employee):  # Inheriting from Employee class
    raise_amount = 1.10  # Overriding class variable for raise amount
    def __init__(self, first, last, pay, prog_lang): # Constructor method
        super().__init__(first, last, pay)  # Calling the constructor of the base class
        self.prog_lang = prog_lang  # Adding new instance variable for programming language
## Creating Another Derived Class
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): # Constructor method
        super().__init__(first, last, pay)
        if employees is None:  # Avoiding mutable default argument
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp): # Method to add employee to the manager's list
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp): # Method to remove employee from the manager's list
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self): # Method to print all employees under the manager
        for emp in self.employees:
            print('-->', emp.fullname())
            
dev_1 = Developer('John', 'Doe', 50000, 'Python') # Creating an instance of the Developer class
dev_2 = Developer('Jane', 'Smith', 60000, 'Java') # Creating another instance of the Developer class

mgr_1 = Manager('Sue', 'Jones', 90000, [dev_1]) # Creating an instance of the Manager class
print(mgr_1.email)

mgr_1.add_emp(dev_2) # Adding an employee to the manager's list
mgr_1.remove_emp(dev_1) # Removing an employee from the manager's list


mgr_1.print_emps()



class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
## Creating a Derived Class    
class Developer(Employee):  # Inheriting from Employee class
    raise_amount = 1.10  # Overriding class variable for raise amount
    def __init__(self, first, last, pay, prog_lang): # Constructor method
        super().__init__(first, last, pay)  # Calling the constructor of the base class
        self.prog_lang = prog_lang  # Adding new instance variable for programming language
        
dev_1 = Developer('John', 'Doe', 50000, 'Python') # Creating an instance of the Developer class
dev_2 = Developer('Jane', 'Smith', 60000, 'Java') # Creating another instance of the Developer class

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


# Extending Functionality in Derived Class
class Employee:
    raise_amount = 1.04  # Class variable for raise amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
## Creating a Derived Class    
class Developer(Employee):  # Inheriting from Employee class
    raise_amount = 1.10  # Overriding class variable for raise amount
    def __init__(self, first, last, pay, prog_lang): # Constructor method
        super().__init__(first, last, pay)  # Calling the constructor of the base class
        self.prog_lang = prog_lang  # Adding new instance variable for programming language
## Creating Another Derived Class
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): # Constructor method
        super().__init__(first, last, pay)
        if employees is None:  # Avoiding mutable default argument
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp): # Method to add employee to the manager's list
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp): # Method to remove employee from the manager's list
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self): # Method to print all employees under the manager
        for emp in self.employees:
            print('-->', emp.fullname())
            
dev_1 = Developer('John', 'Doe', 50000, 'Python') # Creating an instance of the Developer class
dev_2 = Developer('Jane', 'Smith', 60000, 'Java') # Creating another instance of the Developer class

mgr_1 = Manager('Sue', 'Jones', 90000, [dev_1]) # Creating an instance of the Manager class

print(isinstance(mgr_1, Manager))  # Checking if mgr_1 is an instance of Manager
print(isinstance(mgr_1, Employee))  # Checking if mgr_1 is an instance of Employee
print(isinstance(mgr_1, Developer))  # Checking if mgr_1 is an instance of Developer
