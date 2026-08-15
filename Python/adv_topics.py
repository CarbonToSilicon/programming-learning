###########################################################      Generators

print("Generators    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
def my_generator(a):
	for i in range(a):
	    yield i
	    
r = my_generator(21)

print(next(r))
print(next(r))
print(next(r))
print(next(r))

print("")
for i in r:
		print(i)
print("")

def my_gen():
	print("First item")
	yield 1
	print("Second item")
	yield 2
	print("Third item")	
	yield 3
	
g = my_gen()

print(f"{next(g)}\n")
print(f"{next(g)}\n")

def fibonacci(max):
	a, b = 0, 1
	while a < max:
		yield a
		#return a
		a, b = b, a+b
		
fib  = fibonacci(100)
print(next(fib))
print(next(fib))
print(next(fib))
print(" |")
for a in fib:
	print(a)

def infinite():
	a, b = 0, 1
	while a < b:
		yield a
		a = b
		b += 1

got = infinite()
print(f"{next(got)}\n")
print(f"{next(got)}\n")


###########################################################      Iterators
print("\n")
print("Iterators    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

list_a = ['a', 'b', 'c', 'd', 'e', 'f']

ab = iter(list_a)

print(next(ab))
print(next(ab))
print(next(ab))
print(next(ab))

my_list = ['a0', 'b0', 'c0', 'd0', 'e0', 'f0']

print("")
iter_obj = iter(my_list)
while True:
	try:
		element = next(iter_obj)
		print(element)
	except StopIteration:
		break

				
###########################################################      Moduler Programming
print("\n")
print("Moduler Programming    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


import os

print(f"{dir(os)}\n")
print(f"{os.getcwd()}\n")
print(f"{os.listdir()}\n")

import my_modules

data = [1,2,3,4,"five",6,7,8,9,0]
print(f"{my_modules.counter(data)}\n")

from my_modules import counter as a_counter

print(f"{a_counter(data)}\n")

print(f"{dir(my_modules)}\n")

import sys
print(f"{sys.path}\n")


###########################################################      Python Packages (PENDING)
print("\n")
print("Python Packages (PENDING)    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

#import sys

#sys.path.append("/data/data/com.termux/files/home/storage/shared/Documents")
         
#import Python_pkg.module0 

#data = [34, 12, 0]
#print(f"{module0.adder(data)}\n")


###########################################################        List Comprehension
print("")

print("List Comprehension    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [each_fruit for each_fruit in fruits if "a" in each_fruit]
print(f"{newlist}\n")

s_list = [each for each in "humans"]
print(f"{s_list}\n")

num_list = [x for x in range(20) if x % 2 == 0]
print(f"{num_list}\n")

obj = ["even" if i % 2 == 0 else "odd" for i in range(20)]
print(f"{obj}\n")

def double(x):
	return x**2
	
y = [double(i) for i in range(11)]
print(f"{y}\n")

text = "Life, uh, finds a way, in a great way indeed."
vowels = {each_letter for each_letter in text if each_letter in ["a", "e", "i", "o", "u"]}
print(f"{vowels}\n")

squares = {i:  i**2 for i in range(11)}
print(f"{squares}\n")


###########################################################        Regular Expression
print("")
print("Regular Expression    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

import re

#re.match()

pattern = "^a...s$"
string = "abyss"
result = re.match(pattern, string)
print(result)

result = re.match("^a...s$", "abbbyss")
print(result)

string = "The Titanic was released in 1998.\nthe Titanic was fun."
result = re.match("[abce]", string)
print(result)

result = re.match("[abceT]", string)
print(f"{result.span()}\n")

#re.search()

result = re.search("^[ctw]", string, re.MULTILINE)
print(f"{result.span()}\n")

#re.findall()

string = "111 film Titanic was released in 1998"
result = re.findall(r"[abc]", string)
print(f"{result}\n")

############
print(f"############\n")
print(re.search(r"..", "a"))				  # "." any single char (except newline "\n")
print(re.search(r"..", "ac"))
print(re.search(r"..", "acd"))
print(re.search(r"..", "acde"))
print(f"{re.findall(r"..", "acde")}\n")

print(re.search(r"^a", "a"))                # "^." starts with
print(re.search(r"^a", "abc"))
print(re.search(r"^a", "bac"))
print(re.search(r"^ab", "abc"))
print(f"{re.search(r'^ab', 'acb')}\n")

print(re.search(r"a$", "a"))               # ".$" ends with
print(re.search(r"a$", "formula"))
print(f"{re.search(r"a$", "cab")}\n")

print(re.search(r"ma*n", "mn"))       # ".*" zero or more
print(re.search(r"ma*n", "man"))
print(re.search(r"ma*n", "maaan"))
print(re.search(r"ma*n", "main"))
print(f"{re.search(r"ma*n", " woman")}\n")

print(re.search(r"ma+n", "mn"))      # ".+" one or more
print(re.search(r"ma+n", "man"))
print(re.search(r"ma+n", "maaan"))
print(re.search(r"ma+n", "main"))
print(f"{re.search(r"ma+n", "woman")}\n")

print(re.search(r"ma?n", "mn"))       # ".?" one or zero
print(re.search(r"ma?n", "man"))
print(re.search(r"ma?n", "maaan"))
print(re.search(r"ma?n", "main"))
print(f"{re.search(r"ma?n", "woman")}\n")

print(re.search(r"a{2,3}", "abc dat")) # ".{n,m}" at least n and at most m repetition of  the pattern
print(re.search(r"a{2,3}", "abc daat"))
print(re.findall(r"a{2,3}", "aabc daaat"))
print(f"{re.findall(r"a{2,3}", "aabc daaaat")}\n")

print(re.search(r"[0-9]{2,4}", "ab123csde")) # e.g.
print(re.findall(r"[0-9]{2,4}", "12 and 345678"))
print(f"{re.search(r"[0-9]{2,4}", "1 and 2")}\n")

print(re.search(r"[0-9]{2}", "ab123csde")) # ".{m}" exact repetition of the pattern

for i in range(1, 7):									# e.g.
	s = f"x{'-' * i}x"
	print(f"{i}	{s:12}", re.search("x-{2,4}x",s))
	
print("")
print(re.findall(r"a|b", "cde"))			# ".|." or operator (alteration)
print(re.findall(r"a|b", "ade"))
print(f"{re.findall(r"a|b", "acdbea")}\n")

print(re.findall(r"(a|b|c)xz", "ab xz")) # "(..)" group sub-patterns
print(re.findall(r"(cat|dog)xz", "dogxz"))
print(f"{re.findall(r"(a|b|c)xz", "axz cabxz")}\n")

print(re.search(r"(ba[rz]){2,4}(qux)?", "bazbarbazqux")) # e.g.
print(re.search(r"(ba[rz]){2,4}(qux)?", "barbar"))







