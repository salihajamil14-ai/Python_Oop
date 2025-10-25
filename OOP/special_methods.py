# Special (Magic/Dunder) Methods in Python
# Implementing Special Methods in a Class

# Making a Class with Special Methods
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
     
# Using Special Methods
emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

print(1 + 2)  # Using built-in addition operator
print('a' + 'b')  # Using built-in string concatenation

print(emp_1)  # Default string representation of the object

print(repr(emp_1))  # Official string representation of the object
print(str(emp_1))  # Informal string representation of the object

print(emp_1.__repr__())  # Calling __repr__ method directly
print(emp_1.__str__())  # Calling __str__ method directly

print(1 + 2)  # Using built-in addition operator
print(int.__add__(1, 2))  # Using __add__ method of int class directly
print(str.__add__('a', 'b'))  # Using __add__ method of str class directly

print((len(emp_1)))  # Using built-in len() function
