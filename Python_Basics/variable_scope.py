# Vairable Scope Examples in Python

# Builtin scope
import builtins



x = 'global x'

def test():
    y = 'local y'
    print(y)
    
test()

#print(y)  # This will raise a NameError because y is not defined in the global scope   
def test():
    y = 'local y'
    print(y)
    print(x)
    
test()
print(x)
 
def test(z):
    x = 'local x'
    print(z)
    
test('local z')


m = min([5, 2, 9, 1])
print(m)  # Output: 1

print(dir(builtins)) # Lists all built-in names, including 'min'



def outer_function():
    outer_var = 'outer variable'
    
    def inner_function():
        inner_var = 'inner variable'
        print(outer_var)  # Accessing variable from the outer function scope
        print(inner_var)  # Accessing variable from the inner function scope
    
    inner_function()
    print(inner_var)  # This will raise a NameError because inner_var is not defined in this scope
    
