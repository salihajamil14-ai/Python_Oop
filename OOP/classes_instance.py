class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        pass
emp1= Employee()
emp2= Employee()

print(emp1)
print(emp2)

emp1.first = 'Saliha'
emp1.last = 'Jamil'
emp1.email = 'saliha.jamil@company.com'
emp1.pay = 70000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'Test.User@company.com'
emp2.pay= 60000

print(emp1.email)
print(emp2.email)