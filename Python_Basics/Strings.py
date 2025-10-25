message= ('Hello World')
print(message)
#Dealing with quotes in strings
message1 ="Bobby's World"
print(message1)
#Indexing
message2=('Hello World')
print (message2[10])

print (message2[0:5])
print (message2[6:])# slicing 
#Uppercase, lowercase, count, find, replace
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))
print(message.replace('World','Universe'))
#Concatenation
greeting='Hello'
name='Saliha'
message3= greeting + name
print(message3)
message3= greeting + ', ' + name + '. Welcome!'
print(message3)
message3= '{}, {}. Welcome!'.format(greeting,name)
print(message3)
message3= f'{greeting}, {name}. Welcome!'
print(message3)

print(dir(name))#list of all attributes and methods for an object
print(help(str))#detailed info on the str class
print(help(str.lower))#detailed info on the lower method of str class