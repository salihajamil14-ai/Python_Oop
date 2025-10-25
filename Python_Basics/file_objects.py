# File Objects in Python
# File objects are used to read from and write to files on your computer.
# Reading From a File


f = open('test_file_object.txt', 'r')  # Open a file in read mode
print(f.name)  # Output: test.txt
print(f.mode)  # Output: r

f.close()  # Close the file after finishing operations to free up resources

with open('test_file_object.txt', 'r') as f:  # Using 'with' statement to handle file
    pass

print(f.closed)  # Output: True, file is closed after exiting 'with' block

with open('test_file_object.txt', 'r') as f:
    f_contents = f.read()  # Read the entire file
    print(f_contents)  # Output: This is a test file.
    
with open('test_file_object.txt', 'r') as f:
    f_contents = f.readlines()  # Read lines into a list
    print(f_contents)  # Output: ['This is a test file.\n', 'This is the second line.\n',
    
with open('test_file_object.txt', 'r') as f:
    f_contents = f.readline()  # Read one line at a time
    print(f_contents)
    f_contents = f.readline()
    print(f_contents)  # Output: This is a test file.
    
with open('test_file_object.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents, end='') # Output: ['This is a test file.\n', 'This is the second line.\n']
    
    f_contents = f.readlines() # No more lines to read, returns []
    print(f_contents, end='')  # Output: [] 

with open('test_file_object.txt', 'r') as f:
    for line in f:
        print(line, end='')  # Output: This is a test file.

with open('test_file_object.txt', 'r') as f:
    f_contents = f.read(100)  # Read first 100 characters
    print(f_contents, end='')  # Output: This is a test file.
    
    f_contents = f.read(100)  # Read next 100 characters
    print(f_contents, end='')  # Output: This is the second line.
    
    f_contents = f.read(100)  # No more characters to read, returns ''
    print(f_contents, end='')  # Output:
    
with open('test_file_object.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
        
with open('test_file_object.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())  # Output: 10, current file cursor position
    
with open('test_file_object.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)  # Read first 10 characters
    print(f_contents, end='')
    
    f.seek(0)  # Move file cursor back to the beginning
       
    f_contents = f.read(size_to_read) # Read next 10 characters
    print(f_contents) # Output: This is the second line.
    

# Writing to a file

with open('test_file_object2.txt', 'w') as f:
    pass  # Creates a new file or truncates existing file

with open('test_file_object2.txt', 'w') as f:
    f.write('Test')  # Write 'Test' to the file

with open('test_file_object2.txt', 'w') as f:
    f.write(' Test2')  # Append ' Test2' to the file
    
with open('test_file_object2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Rewritten Test')  # Overwrites beginning of the file

# All combined operations

with open('test_file_object.txt', 'r') as rf:
    with open('test_file_object3.txt', 'w') as wf:
        for line in rf:
            wf.write(line)  # Copy contents from one file to another
    
    #Photos can also be used

    