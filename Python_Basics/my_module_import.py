# Import Modules and Exploring The Standard Library

print('imported my module...')

test = 'This is a test string from import_modules.py'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
