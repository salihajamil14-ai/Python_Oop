if True:    
    print("Condition was True")   
if False:    
    print("Condition was False")      
language = "Python"
if language == "Python":    
    print("Condition was True")
    
    # Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language1 = "Java"
if language1 == "Python":    
    print("Language is Python")
elif language1 == "Java":    
    print("Language is Java")   
else:    
    print("No match")
    
#and, or, not
user="Admin"
logged_in=True

if user == "Admin" and logged_in:
    print("ADMIN PAGE")
else:
    print("Bad Creds")

user1="Admin1"
logged_in=False
if not logged_in:
    print("Please log in")
else:
    print("Welcome")
    
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(id(a))
print(id(b))            
print(a == b)
print(id(a) == id(b))


#Falsey values:
# False
# None
# 0
# 0.0
# ""
# []
# {}    

condition = None
condition2 = 0
condition3 = "Test"
if condition2:    
    print("Evaluated to True")
else:    
    print("Evaluated to False")

if condition3:    
    print("Evaluated to True")
else:    
    print("Evaluated to False")