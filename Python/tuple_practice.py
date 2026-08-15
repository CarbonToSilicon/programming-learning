cars = ("Audi", "Mercedes", "Ferrari", "BMW", "Ford")
print(type(cars))
print(cars[1])
print(cars[0:1]) # ('Audi',)
#cars.remove("Audi")  #error 
city = ('London',)  #single item tuple
print(type(city))
city = ('NYK')
print(type(city))
names = tuple('Dog',)
#names = tuple('Ray', 'John', 'Rihana', 'Brien', 'Mark')  #error
print(type(names))
ages = [40, 30, 12, 33]
ages = tuple(ages)
print(type(ages))
print(ages)
countries = ('USA', 'UK', 'India', 'China', 'Germany')
print(countries)
#countries[1] = 'Japan' #error
c = list(countries)
c[1] = "Japan"
countries = tuple(c)
print(countries)
print("Japan" in countries)
#countries.pop["India"]  #error
del countries
#print(countries)  #error
fruits = ("Mango", "Grapse", "Chery", "Apple", "Papaya")
for i in fruits:
    print(i)

######################     BOOK     ######################
t = 'a', 'b', 'c', 'd', 'e'
print(type(t)) #tuple
t = ('a', 'b', 'c', 'd', 'e')
print(type(t))
a = 'a',
print(type(a)) #tuple
t = ('A',) + t[1:]
print(t)
print((0, 1, 2) < (0, 3, 4))
print((0, 1, 200000) < (0, 3, 4))
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t =list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(t)
print(res)
m = ('have', 'fun')
x, y = m
print(x)
print(y)
m = ['have', 'fun']
x, y = m
print(x)
print(y)
m = ('have', 'fun')
x = m[0]
y = m[1]
print(x)
print(y)
x, y = y, x
print(x)
print(y)
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)
d = {'b':1, 'a':10, 'c':22}
t = list(d.items())
print(t)
