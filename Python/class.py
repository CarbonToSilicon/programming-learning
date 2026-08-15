#### Class and Objects #### - Class is a blueprint for creating objects.

##creating class
#class Students:
#	name = "Tushar" #always same
##creating objects (instance)
#hi = Students()
#print(hi)
#print(hi.name)
#hi1 = Students()
#print(hi.name)

##creating class
#class Car:
#	color = "blue"
#	brand = "mercedes"

##creating objects (instance)	
#car1 = Car()
#print(car1.color, car1.brand)
#print(Car().color)

#### __init__  function (constructor) #### - all classes have a function called __init__(), which is always executed when the object is being initiated. Wether you create or not. "__init__" means initialization

##creating class
class Students:	
	##  *The (self) parameter is a referance to the current instance of the class, and is used to accss variables that belongs to the class. And we must pass this "self" parameter in every function in the class
	##this is a default constructor
	def __init__(self):
		pass
	
	##this is a parameterized constructor
	def __init__(self, name, Marks):
		print(self)
		print("object initiated!")
		self.name = name
		self.marks = Marks
		
s1 = Students("Tushar", 90)
print(s1)
print(s1.name)

s2 = Students("Abhishek", 89.9)
print(s1.name, s1.marks)
print(s2.name, s2.marks)		


#### Class & Instance Attributes #### - variables inside a class and its functions

#                                     Class
#   					___________|__________
#                       |                                   |
#        *data(attributes)        methods(functions)

#class Student:

#	college_name = "SRK"   # *class Attribute, do not change for each object
#	name = "anonymous"   # *class attr
#	def __init__(self, name, Marks):
#		self.name = name    # obj Attribute, change with each object intialization
#		self.marks = Marks  #obj attr
		
#s1 = Student("T", 98)
#print(s1.college_name, s1.name, s1.marks)

#### Methods #### - Methods are functions that belong to objects

#                                     Class
#   					___________|__________
#                       |                                   |
#        data(attributes)        *methods(functions)

#class Students:
#	clg_name = "Apna College"
	
#	def __init__(self, student, Score):
#		self.student = student
#		self.score = Score
#	def welcome(self):
#		print(f"Welcome student, {self.student}.\nYou scored {self.score} in your last test.")

#student1 = Students("Tushar", 89)
#student1.welcome()
#print(student1.student, student1.score)

#### Practice 1 ####

#class Students:
#	def __init__(self, name, marks):
#		self.name = name
#		self.marks = marks
		
#	def get_avg(self):
#		sum = 0
#		avg = 0
#		for i in self.marks:
#			sum += i
#			avg = sum//len(self.marks)
#		return avg
		
#s1 = Students("Abhishek", [56, 36, 46])
#print(s1.name)
#print( s1.get_avg())

#s1.name = "Ironman"
#print(s1.name, s1.get_avg())

#### Static Method #### - Methods that don't use the self parameter (work at class level)

#class Students:
#	def __init__(self):
#		pass
#	# *Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modfying it
#	@staticmethod   # decorator
#	def college():
#		print("Apna college")
#		
#s1 = Students()
#s1.college()



