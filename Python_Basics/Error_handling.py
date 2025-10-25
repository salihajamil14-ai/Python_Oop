# Try/Except for error handling

# Handling general exceptions
try:
    f = open("non_existent_file.txt", "r")
except Exception:
    print("An error occurred while trying to open the file.")
    
   
# Handling specific exceptions 
try:
    f = open("non_existent_file.txt")
    var = bad_var # This will raise a NameError
    
except FileNotFoundError:   # Specific exception for file not found
    print("The file was not found.")
except Exception:
    print("An error occurred while trying to open the file.")
    
    
try:
    f = open("non_existent_file.txt")
    var = bad_var # This will raise a NameError
    
except FileNotFoundError as e:   # Specific exception for file not found
    print(e)
except Exception as e:
    print(e)  # Print the exception message
else:
    print(f.read())  # Only runs if no exception occurred
    f.close()  # Ensure the file is closed
    
  
# Using finally to execute code regardless of exceptions  
try:
    f = open("test_file_object.txt")
    print(f.read())
    f.close()
    
except FileNotFoundError as e:   # Specific exception for file not found
    print(e)
except Exception as e:
    print(e)  # Print the exception message
else:
    print(f.read())  # Only runs if no exception occurred
    f.close()  # Ensure the file is closed
    
    
try:
    f = open("non_existent_file.txt")
except FileNotFoundError as e:   # Specific exception for file not found
    print(e)
except Exception as e:
    print(e)  # Print the exception message
else:
    print(f.read())  # Only runs if no exception occurred
    f.close()  # Ensure the file is closed
finally:
    pass  # Code here will run no matter what