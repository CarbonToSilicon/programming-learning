# ---------- 6.9  String .methods -----------

eg = 'Hey I welcome you.'
print(type(eg))
print()
print(dir(eg))
print()
print(help(str.istitle))
print()

eg0 = "My name is T and I live in India."
print(eg0.lower())

eg1 = "I will be a python programmer by the end of this year (2025/10)."
print(eg1.upper())

eg2 = " Hey! \n"
print(eg2.strip())

eg3 = ("it's true.")
print(eg3.replace('t', 'a'))
az = 'not end'
print(eg3.replace('true', az))

eg4 = "This took me a lot of time to find my path compare to other"
print(eg4.find('took me'))
print(eg4.find(' look me'))
print(eg4.find('took me', 5)) # the second argument is the index number where the function will start to work from.
# if the output is (-1) than it means it could not found what it was finding

eg5 = 'machine'
print(eg5.startswith('mac'))
print(eg5.startswith('Mac'))

eg6 = 'Elephent'
print(eg6.endswith('ent'))
print(eg6.endswith('ents'))
print(eg6.endswith('hen'))

eg7 = "But still I am not aware of the journey and other paths in this journey."
print(eg7.split('.'))
print(eg7.split(' '))
print(eg7.split('I'))

eg8 = ['yellow', 'red', 'black', 'white', 'maroon', 'green', 'sky-blue']
print(eg8) # in this output you will see words separated by (', ') in the list but when we use .join() we don't encounter these characters because this (', ') char is just use for humans to identify the list but the computer store them in different way and remove this(', ') in this in any other expression when we change the data type of list or extract objects of the list.
print(''.join(eg8)) # the argument we provide to the .join() method is different from other string methods because it takes the main data we want to work upon like built in funtions. And use string object (before dot notation) as the basis for the method and there are more such a this type of methods.
print(' '.join(eg8))

eg9 = "I hope this is gonna be a lot more valuable than a BA degree and accounting job."
print(eg9.count('a'))
print(eg9.count('A'))
print(eg9.count('lot'))
print(eg9.count(' '))
print(eg9.count('')) # this empty arugument counts all the characters from the given data.
print(eg8.count('a')) # this is working on a list not a string




