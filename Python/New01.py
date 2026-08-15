###################A LIST IS A SEQUENCE###################
dogs = ["husky", "bull", "germon"]  ########################
ages = [5, 10, 12, 20, 30]  ####################### 
list1 = ['spam', 2.3, 5, [25, 30]]  ######################## 
empty_l = []  ########################
print(f"{dogs}\n{ages}\n{list1}\n{empty_l}")

###################LISTS ARE MUTABLE##################
print(f"\n{dogs[0]}")

ages[1] = 8
print(ages)

print("bull" in dogs)
print("Brie" in dogs)

###############TRAVERSING A LIST####################
print("\n")
for dog in dogs: print(dog)

for i in range(len(ages)):
  ages[i] = ages[i] * 1.5
print(ages)

for x in empty_l:
  print("This will never happen!")

##############LIST OPERATION#################
a = [1, 2, 3] ########################
b = [4, 5, 6]  ########################
print(f"\n{a + b}")

c = [0]  ##################
print(c * 5)

d = [1, 2]  ########################
print(d * 3)

###############LIST SLICES####################
t = ['a', 'b', 'c', 'd', 'e', 'f']  ##############

print(f"\n{t[1:3]}")
print(t[:5])
print(t[2:])
print(t[:])

t[2:4] = ["x", "y"]
print(t)

#############LIST METHODS###############
t.append('g')
print(f"\n{t}")
t0 = t[:]
t0.append(['h', 'i']) # it is wrong practice to append multiple objects
print(t0)

t1 = ['h', 'i']
t.extend(t1)
print(t)

gh = t.sort()  #Wrong practice
print(t)
print(gh)
#g = t.sorted()
#print(g)

#########DELETING ELEMENTS###########
s = t.pop(0)
print(f"\n{t}")
print(s)

del t[1]
print(t)

t.remove('i')
print(t)

del t[0:2]
print(t)

################LISTS AND FUNCTION#########################
nums = [3, 41, 12, 9, 74, 15]
print(f"\n{len(nums)}")
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

total = 0
count = 0
while (True):
  inp = input("Enter a number (type 'ok' to get average): ")
  if inp == 'ok': break
  value = float(inp)
  total += value
  count += 1
average =  total / count
print('Average:', average)

numlist = list()
while (True):
  inp = input("Enter a number (type 'ok' to get average): ")
  if inp == 'ok': break
  value0 = float(inp)
  numlist.append(value)
average0 = sum(numlist) / len(numlist)
print('Average:', average)

#########################LISTS AND STRINGS##########################
y = "spam"
y1 = list(y)
print(f"\n{y1}")
v = "pining for the fjords"
t = v.split()
print(t)

y = 'spam-is-harmful'
delimiter = "-"
y1 = y.split(delimiter)
print(y1)

f = ["pining", "for", "the", "fjords"]
delimiter = " "
f1 = delimiter.join(f)
print(f1)

####################PARSING LINES###############################
# print("\n")
# fhand = open('mbox-short.txt')
# for line in fhand:
#   line = line.rstrip()
#   if not line.startswith("From "): continue
#   words = line.split()
#   print(words[2])
  
###################OBJECT AND VALUES############################
ac = "banana"
ad = "banana"
print(f"\n{ac is ad}")

ac = [1, 2, 3]
ad = [1, 2, 3]
print(a is b)

######################ALIASING##########################
A = [1, 2, 3]
B = A
print(A is B)

B[0] = 17
print(A)

######################LIST ARGUMENTS#########################
def delete_head(t):
  del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t1 = [1, 2]
t3 = t1 + [3]
print(t3)
print(t1 is t3)

def bad_delete_head(t):
  t = t[1:]       #Wrong
  
def tail(t):
  return t[1:]
  
letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)
