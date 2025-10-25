from calendar import month


def hello_func():
    pass
print(hello_func())  # This will print None since the function does not return anything.
print(hello_func)    # This will print the function object itself.
print('Hello Function!')  # This will print the string 'Hello Function!'.
hello_func()  # This will call the function, but since it does nothing, there will be no output.    
def hello_func():
    return 'Hello Function!'    
print(hello_func())  # This will print 'Hello Function!' since the function now returns that string.
print(hello_func)    # This will still print the function object itself.    
print('Hello Function!')  # This will print the string 'Hello Function!'.
hello_func()  # This will call the function and return 'Hello Function!', but since we
print(hello_func().upper())  # This will print 'HELLO FUNCTION!' by calling the function and converting the result to uppercase. we don't do anything with the return value, there will be no output.   
def hello_func(greeting):
    return '{} Function!'.format(greeting)
print(hello_func('Hi'))
def hello_func(greeting, name='You'):  
    return '{}, {}!'.format(greeting, name)
print(hello_func('Hi'))
print(hello_func('Hi', name='Corey'))
def student_info(*args, **kwargs):  
    print(args)
    print(kwargs)
student_info('Math', 'Art', name='John', age=22)
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(courses, info)
student_info(*courses, **info)  # This will unpack the list and dictionary into separate arguments.


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]
print(is_leap(2017))  # False
print(days_in_month(2017, 2))  # 28

