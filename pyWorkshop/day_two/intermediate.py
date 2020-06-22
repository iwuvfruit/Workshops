my_data = "this, is, a, comma, seperated, string" #this looks like a svc file
#we can split this data
my_data.split(",")
student = "Marry,8,Math"
student.split(",") #we get back list
name, age, subject = student.split(",") #unpacking 
my_list = my_data.split(",")
",".join(my_list)#join back with , into one string
int("5") #int
float("4.0") # float
"100"
str(50)
#"Today is the" + 30 #this will give you an error can't concatenate str with in
"Today is the" + str(30)
float("3.14")
#string is a list of sequence
greeting = "hello"
list(greeting)
",".join(list(greeting))
my_chars = list(greeting)
"".join(my_chars)
csv_row = "the,quick,brown,fox"
csv_row.split(",")
names = ["nina", "bob", "jeff", "madeline","nina"]
#set can be used to remove the duplicates
set(names)
sorted(set(names)) #list has order but sets do not 

#list comprehension using for loop
upper_names = []
for name in names:
	upper_case_name = name.upper()
	upper_names.append(upper_case_name)

[name.upper() for name in names]
range(4) #0,1,2,3 generated range between 0 and 4 on the fly
#to peek inside of range
list(range(4))
list(range(1, 4))
list(range(1, 5, 2))
[num * num for num in range(6)]
#I want to return tuple
[("length", len(name))for name in names]
#f string
name = "Nina"
f"The name is {name}"
"".join([f"name is {name}"for name in names])
[num * num for num in range(6)]
bool(6 % 2) #flase
bool(1)
bool(-1)
bool(0)
bool(6 % 2 == 0) #true 
[num * num for num in range(6) if num % 2 ==0]
even_squares = [num * num for num in range(6) if num % 2 ==0]
",".join([str(even_square) for even_square in even_squares])
#now '0,4,16' rather than [0,4,16]
squares = [num * num for num in range(6)]
sum(squares)
min(squares)
max(squares)
sorted(squares)
sorted(squares, reverse=True)
lottery_numbers_string = "4, 5, 134, 10"
#max takes list
#list needs to be in numbers
lottery_numbers_string.split(",") #list of strings
print(lottery_numbers_string.split(", "))
max([int(num) for num in lottery_numbers_string.split(", ")])

#4 different data types 
#list, tuple, set, dictionaries
#they all have comprehensions
#set comprehensions
type({}) #dictionary
type({1}) #set 
{num * num for num in range(11)} #sets are unordered
#difference between set and dictionary is that dictionary is a key value pair
{num: num*num for num in range(11)}
['Nina', 'Max', 'Jimmy']
[f"The name is {name}" for name in names]
dups_names = ["nina", "max", "nina"]
set(dups_names)
print(set(len(name) for name in dups_names))
#generator comprehension
#like range the value is calculated as we need it 
range(5)
print(len(name) for name in dups_names)
#we get generator object 
print(max((len(name) for name in dups_names)))
min((len(name) for name in dups_names))

x = (num * num for num in range(6))
#I can't do x[0], the way we get this generation is in for loop 
for num in x:
	print(num)
#generator structure is not in memory, lists have all the items in it and in the memory 
#slicing:way to create larger lists
my_string = "Hello World"
my_string[0] #this will return h
my_string[-1] #return d
my_string[0:5] #hello 5 is excluded 

names = ["Nina", "Max", "Rose", "Jimmy"]
names[0]
names[-1]
names[:2]
names[2:4]
names[2:]
new_names = names
new_names.append("Phillip")
#now names and newNames are both affected so better to create an original
names[:] #I get a copy of it
new_names = names[:]
new_names.append("Rose")
print(names)
print(new_names)

my_string = "Hello World"
my_string[-1] #d
my_string[-2] #l 
#it's circular 
my_list = list(range(10))
my_list[::2] #third one is step 
my_list[::-1]#going backward
my_list[1:7:2]
#can't do slicing with set and dictionary because they are not ordered
#if I can play with index then I can slice it 

#Zip 
{num: num * num for num in range(11)} #dictionary
squares = {num: num*num for num in range(11)} 
squares.keys()
squares.values() 
squares.items() #list of tuples 
players = ["nina", "bob", "alice"]
scores = [100, 5, 97]
zip(players, scores) #generator?
for item in zip(players, scores):
	print(item)
#we have a list of tuples
for name, score in zip(players, scores):
	print(f"Name:{name} had a score of {score}")
#using list comprehension
[f"name {name} had a score{score}" for name, score in zip(players, scores)]
my_list = [1,2,3]
my_list2 = ["a", "b"]
zip(my_list, my_list2) #3 won't make it because it pairs in order 
list(zip(players, scores))
dict(zip(players, scores)) #tuple has to have two variables, key and value

#comprehension, slicing, zip excercise
my_list = [num for num in range(100) if num % 2 == 0]
import random 
help(random.randint)
random.randint(0, 100)
my_dict = {num: random.randint(0, 100) for num in my_list}
my_dict.values()
set(my_dict.values())
{num for num in my_dict.values()}

range(100)
list(range(100))

#oop
#allows us to organize code into objects/classes
#language model where behaviors/properties are organized to objects
#everything in python is an object
#for instance for integer you can do int(5)
#good for readability,maintaibility/overall structures

#classes:
#everything in python is an instance of class 
int(5)
type(int(5)) #class is int
type(int) #class is a type 
#class is like a template and you can make an instances using the class
class Car:
	runs = True
	number_of_wheels = 4
	#to instantiate, use initializer
	#double underscore -> dunder -> special, hapeens under the hood
	#self is required argument for initiallizer 
	#when you make binding, python always passes self under the hood 
	#so if I don't have self there it'll give take 0 positional argument but 1 given
	def __init__(self, name):
		print("new car")
		self.name = name #name is guaranteed t o be there for a variable 

	#dunder init method gets called under the hood when we create a new instance of class

	#if I do my_subaru then I get Car object at 0x12312312
	#we want this to be human readable not repr 
	def __str__(self):
		return f"My car the {self.name} currently {self.runs}"
		#print doesn't return 
		#x = print("hi")
		#type(x) is none
		#we actually want to return string

		#now I create a new car my_car = Car("mustang")
		#str(my_car) returns the statement
	def __repr__(self):
		return f"Car({self.name})"
		#so when I make a new car and call repr I get Car(mustang)



	def start(self): #self signifies it's a instance method
		#I don't want to add name evertyime I start the car so it makes sense to put name in the init
		#self is associated with instances
		self.name = name 
		if self.runs:
			print(f"{self.name} Car is started")
		else:
			print(f"{self.name} is broken")
	#class method
	#it doesn't take self, instead it takes different argument
	#argument, cls: as convention
	#now you can access class variables 
	@classmethod
	def get_number_of_wheels(cls):
		return cls.number_of_wheels

from intermediate import Car
type(Car)
Car.runs
Car.name #error, no attribute
my_subaru = Car() 
type(my_subaru) #this is an instance of class
my_subaru.start("subaru")
my_subaru.name #it's associated with instance not class so this time it works
#no need getter and setter to modify stuff in python
my_subaru.runs = False #I can change without getter/setter
my_subaru.start("subaru")#now it returns broken 
mustang_car = Car()
mustang_car.runs #this will return true, the change I made to subaru only effects subaru

#now with initialized method
my_subaru = Car("my_subaru")
my_mustang = Car() #if I don't pass in name argument, I get type error that it's missing positional argument

#I wasn't able to access the name from just a type
Car.get_number_of_wheels() #this is a type, not a instance 
#you can call these class methods on instances too 
my_subaru.get_number_of_wheels()
type(Car) #this is a type
type(my_subaru) #this is car
type(int) #this is a type
type(int(5)) #this is int 
isinstance(42, int) #true
isinstance("hello world", str) #true
isinstance(42, str) #false
isinstance(my_subaru, int) #false
isinstance(my_subaru, Car) #true
#don't use this in production code 
isinstance(True, int) #true
bool(0) #false 
bool(1) #true 
#booleans are sub class of int 
True + True #will give two 
set(0, 1, True, False)
#ths returns 0 and 1
#everything in class is a subtype of object 
[1, 2, 3]
#string representation
str([1, 2, 3]) #human readabile string value
repr([1,2,3]) #reper: how would I tell python to create a new instance 

import datetime
#just like Cars.cars
now = datetime.datetime.now()
str(now) #human readable 
repr(now) #what argument I need to pass to instiantiate this


###say I have a new file named vehicle.py and want to share properties with Car
#motorcycle has 2 runs but still runs
#so we use inheritance
#issubclass(bool, int)
#bool took all classes of int and added more 
class Vehicle:
	#default argument has to come late
	def __init__(self, make, model, fuel="gas"):
		self.make = make
		self.model = model
		self.fuel = fuel
	def is_eco_friendly(self):
		if self.fuel == "gas":
			return False
		else:
			return True 
#inherits and extends from vehicle
class Car(Vehicle):
	#constructor
	def __init__(self, make, model, fuel="gas", numm_wheels=4):
		super().__init__(make, model, fuel)
		self.numm_wheels = numm_wheels

#now I can say 
four_by_four = Vehicle("zoom", "goes fast", "cooking oil")
four_by_four.make
four_by_four.fuel
my_subaru = Cars("subaru", "cross treck", 
	fuel="diesel")
my_subaru .numm_wheels #it's default so it's t here 
four_by_four.numm_wheels #vehiclel has no attribute wheels
four_by_four.is_eco_friendly
my_subaru.is_eco_friendly
#python: you can have multiple inheritance 

########################################################
#Exceptions 

user_input = 'a'
try:
	int(user_input)
	num = int(user_input) #this code won't run 
except ValueError:
	print("that's not a number")
#the code in except block runs 

#you can have multiple errors with tuple, if any of those exceptions caught
d = {1:1}
user_input = 2
try:
	int(user_input)
	d[user_input]
except(ValueError, KeyError):
	print("noo")

try:
	int("a")
except ValueError as e: #gives message for the exception
	print("oh no", e)

def division(num):
	try:
		result = 3.14 / num
	except ArithmeticError: #this is more general one
		print("we had a general math error")
	except ZeroDivisionError: #this is more specific
		print("divided by zero error")
#I used general one so it swallowed more helpful one
#so use more specific one first 

#dont do this
try:
	int("a")
except Exceptions:
	pass 
#don't swall exception, do something

issubclass(ValueError, Exceptions) #true 
#Exception is general

class MyCustomException(Exception):
	pass 

raise MyCustomException() #custom exception error 

class IncorrectValueError(Exception):
	def __init__(self, value):
		message = f"Got a badvalue: {value}"
		super().__init__(message) #how do I call exception class and pass my new message
		#Exception in general takes a message

my_val = 998
if my_val > 999:
	raise IncorrectValueError(my_val)

#don't do this
raise Exception("whatever message I want")



