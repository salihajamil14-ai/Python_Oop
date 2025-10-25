# Property Decorators (Getters, Setters, and Deleters)

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # Getter for email
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property  # Getter for full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # Setter for full name
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter  # Deleter for full name
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Doe')
emp_1.fullname = 'Jane Smith'  # Using the setter to change the full name

print(emp_1.first)  # Accessing the first name after using the setter
print(emp_1.email)  # Accessing the email property
print(emp_1.fullname)  # Accessing the full name property

del emp_1.fullname  # Using the deleter to delete the full name