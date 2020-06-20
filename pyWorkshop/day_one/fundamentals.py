'''
type(42)
type(3/4)
z = int('7')
type(z)
a = float(5)
print(type(a))

rent = 450
per_day = 450 / 30
print(per_day)
name = "young"
print("my name is",name)# notice there's a space
print(f"my name is {name}")
f"hello my name is {name} I pay ${rent / 30} per day"

x = 5
type(x)
print(dir(int)) #all the methods I can use on x
#dir(class) #here int is the class 
def foo():
	print("hello") 
foo()

def meaining_of_life():
	return 42
x = meaining_of_life()

called_foo = foo()
print(type(called_foo))
print(type(x))

def add_numbers(x, y):
	return x + y #x, y only alive within this scope

num = add_numbers(3, 5)
print(num)

def greeting(name):
	greeting = "hello"
	return greeting + name

print(greeting("younggue"))

def foo():
	x= 5
	return
x = foo()
print(type(x))

def add_numbers(x, y):
	return x+y 
add_numbers(3, 5)
#add_numbers(3) #this will give you a type error
def say_greeting(greeting, name):
	print(f"{greeting}, {name}")

say_greeting("hello", "nina")
# the below will overwrite
# this one will pass the default arugment
#make sure default argument comes last 
def say_greeting(name, greeting="hello"):
	print(f"{greeting} {name}")
say_greeting("nina")
say_greeting("nina", "bonjour")

def create_query(language="javascript", num_stars=50, sort="desc"):
	return f"{language},{num_stars},{sort}"

create_query() #this is okay since it's key labeled variable, there are defaults
create_query(language="python") #passing labeled
create_query(num_stars="20", language="ocaml") #because they are labeled, no need to be in order 

def foo(a, b=5):
	return a + b
foo(3)
foo(3, 10)
foo(a=3, b=7) 

#dont do this
def foo(a, b=[]):
	b.append(a)
	print("b is ", b)
foo(5)
foo(6) #it's using the same list over and over 
# so check if b is none then append it 
#because python is dynamic you have to be mindful about naming variable
#so be as explicit as possible 

#inside python function scope changes 

def twitter_info():
	account = "nnja"
	print(f"account inside the function is: {account}")
twitter_info 

#print(account)
#what if I try to use account outside the function
#but then it will show not defined because we declare within the scope of the function
#out side the function we are in a different scope
name = "ninja" 
def try_nchange_name():
	name = "Max"
	print(f"{name} is the answer")
try_nchange_name()
print(name)
#in general, don't have too many floating variables outside scope

#don't do this , source of bugs 
#it doesn't have anything to do scope
#but b is the same list everytime I call
#because this default argument, they get instantiated once when the function is defined
#it won't create a new empty list everytime function will create 
#big bug!! 
def foo(a,b=[]):
	b.append(a)
	print(a)
foo(1)
foo(2)
# do this instead 
def foo(a, b=None): #b is flag,signal for this
	if b is None:
		b = []
	b.append(a)
	print(b)
foo(1)
foo(5)
def add_number(x, y):
	return x + y
add_number(1, 2)
a = 1
b = 1 
add_number(a, b)

#indentation error
# def foo():
# x = 5

x = 1
y = 2
def add_numbers(x, y):
	print(f"inside the func, x:{x}, y:{y}")
	return x + y
print(f"outside the func, x:{x}, y:{y}")
add_numbers(3, 5)

def calculate_numbers(x, y, operation="add"):
	if operation == "add":
		return x + y 
	elif operation =="subtract":
		return x - y

print(calculate_numbers(4, 5))
print(calculate_numbers(4, 5, operation="subtract"))
calculate_numbers(y=3, x=2) #no need to be inorder because I'm passing labels 

== equality to compare for values 
is do they point to the same thing in memory?
is compare for built in types 

[] 
x = list()
print(type(x))

#plural: so probably a collection -> list
names = ["nina", "max", "rose"]
print(names)
#method not on lists but just python built in
print(len(names)) #globally avaliablel 
print(names[0])
print(names[2])
#print(names[3]) index error 
names[1] = "jimmy"
print(names)
#when I declare list, optionally I can do
sam = [
	"ss",
	"aa",
	"mm", #you can have comma here and close
]
#invalid syntax [1, 2, 3 4] you see syntax erro point on the one that's next to it 
#be specific how you format list because list has orders 
#because it has orders you can sort them too

lottery_numbers = [12,1, 4, 231, 321, 232]
#there are two ways sorting in python 
#take the original list and return new one
print(sorted(lottery_numbers)) #built in method 
print(lottery_numbers)
#sorted takes optional default argument
sorted(lottery_numbers, reverse=True) #sorting in back word
#the above returns a copy 

#secod way of sorting lists in python is IN LIST
lottery_numbers.sort() #I'm calling it on my own variable, nothing returns
#we are not getting a new copy 
lottery_numbers.reverse() #doing it in place
#if I want to see all the directory listing of all the avariable methods I call
type(lottery_numbers)
dir(list)
#if I want to get help on some method such as not know what argument to put then
help(list.reverse)



names = ["nina", "max"]
names.append("jimmy")
print(names)
#insert method takes two variables,
#position and value 
names.insert(0, "rose")
print(names)
#help(list.insert)
colors = ["Red", "Blue"]

names.extend(colors) #list has orders 
#looking up if it's in list is very slow operation
#it traverses one by one 
names = ["nina", "max", "philip", "nina"]
print("Rose" in names) #in key workd
print("nina" in names) 
#we can also use index method to find the index
print(names.index("max"))
print(names.index("nina"))
print(names.count("nina"))
names[0] = "young"
print(names)
pos = names.index("philip")
names[pos] = "Lip"
print(names)
len(names)
#index count from zero

#we can remove with remove method
#if there are duplicates, it only removes the first instance it sees
#if we try to remove something that's not there, then we get valueError 
#we can use pop to get the last method or pop at some certain index
#it will also return the popped one 
names.remove("max")
print(names.pop())
names = ["nina", "rose", "max"]
names.pop(1)
len(names)
#use list for storing similar elements 

#mutable item: contents of the items can be changed after declared 
#list can contain any data type
#data structure that can store another data structure
#all the members don't need to be the same
name = [1, "a", True, None]
print(name)
#but generally we don't see this. 

#Tuples are light weight collection that keeps track of related but different items
#while lists are mutable, can add/remove/change value
#tuples are not mutable,once created items can't be changed. 
#tuples are useful things like containing snapshot of data 
#tuples might represent top rows in a spreadsheet 
#they provide security with the data. 
a = ()
type(a)
b = (1)
print(type(b))
#tuples are about commas not just parenthesis
#the comma is the important part
#so we need to add a comma
c = (1,)
print(type(c))
(1,2,3,4,5)

students = ("marcy", 8, "history", 3.5)
students[0]

#students[0] = "nina" type error, it doesn't support item assignment
#it doesn't have pop or remove method 
#data being unchanged ->tuple
#ex)dictionary key needs to be immutable, you can use a tuple 
#you cant use a mutable data type that can be changed 

#tuple unpacking: 
name, age, subject, gpa = students
print(name)
print(age)
#generally nr of variables need to match nr of items in tuples
#otherwise you ll see value error
name, age, subject, _ = students
#then name, age ,subject will be set. _ means throw it away 

x = 1, 2, 3 #I can declare tuple without parenthesis because it's comma that makes it different

def http_status_code():
	return 200, "OK" #the return type is duple
code, name = http_status_code()
print(code)
print(name)
#in tuple, order is reserved 

#sets are data types that allows you to store other immutable type unsorted way
#all the simple types are immutable, string int etc
#item can be set in once, no duplicate
#sets don't have orders, can't access them by position
#very fast membership testing -> it stores hashed value of that type. to check if it's in hash, its fast membership
#on sets, you can have union, intersection etc 

type({}) # this is dictionary
set()#empty set needs to be set this way
{1}
type({1})
names = {"nina", "max", "nina"}
print(names) #duplicate value is just ignored
len(names)
#sets cant contain mutable data type 
#the way that allows you to check quickly is with an algorith hash
#there's a hash function built in python
hash("nina")
#it's there 
#hash([]) #this is a type error, unhashable type-can't hash it 
#{[]} #unhashable, you can only put immutable in sets 
#because sets can't duplicates, it's quick way of duplicating list
names = ["nina", "max", "nina","chang"]
set(names) #sets don't have orders 
#if I try to access it using index -> type error, there's no position 
#adding and removing from sets
colors = {"Red", "Green", "Blue"}
colors.add("pink")
colors.discard("Green")
print(colors)
#colors.remove("not there then error")
colors.discard("even when there's no item, no error")

numbers = {1, 3, 5}
colors.update(numbers)
#both sets are now combined similar to extend
colors.update("nina")
#character is a sequence, so it grabs each individual and add it to the set
print(colors)

#we can use set operations to compare with other sets
#to check if item is in set
colors = {"Red", "Green", "Blue"}
"Blue" in colors
"orange" in colors 
#there's no .index because it's not ordered 
#sets don't have count method

rainbow_colors = {"Red", "orange", "yellow", "green","blue","violet"}
favorite_colors = {"pink", "black", "blue"}
#my_set.union(other_set)
#my_set | other_set //pipe means union
rainbow_colors | favorite_colors #when doing an union: this removed duplicates 
#intersection 
rainbow_colors & favorite_colors
#difference 
rainbow_colors ^ favorite_colors
#there's a lot more such as subset, frozen set: you want your set to be immutable 
#you can do things such as help(set.union)

#what kind of data structure can you sort?
#A) list
#we know list is sortable so we move set to list
list(rainbow_colors) #now it's a list
#dictionaries in python
#key-value pairs 
#mutalbe
#but dictionary keys are only immutable type
#mutable into set then unhashable type, samething for dictionary keys 
#we use dictionaries when we want to quckly access with a particular key

#key is in there or not ->very fast
{} #empty dictionary 
dict() #empty dictionary 
#data structures are usually created with {} () rather than methods
{1:"One"} #one item dictionary
nums = {"one":1, "two":2, "three":3} #key value pairs are seperated by commas
type(nums)
{1:1}
{1:[]} # I can have mutable type as a value
#{[]:1} #unhashable type error

#keys in our ditionaries are not ordered
nums['one'] #we put the key inthere to get the value 
#try to access the dictionaryh by position?
#no because dictionaries are not ordered

nums.get("four") #key not there but no e rror
#nums["four"] #then key error. this gives you explicit error while get method doesnt'
nums.get("one")
nums.get("four", "default value") #if four isn't there print default value

#adding/removing because dictionary itself is mutable
nums["four"] = 4
nums["two"] = "the key is already there duplicate keys okay? you can't because of have hash. it will just overwrite the value there"
"one" in nums
#sets and dictionaries are similar. 
#there''s no duplicates, easy to see if it's in there or not.
colors = {"r":"Red", "g":"Green",2:"update"}
numbers = {1:"One", 2:"two"}
colors.update(numbers)
print(colors) # combined. 

colors = {"Green":["Spinach"]}
vegetables = colors

vegetables["Green"] #this is a list
type(vegetables)
#because it's a list
vegetables["Green"].append("apples")

print(colors) 
#now storing a list of elementss in the key
#dictionaries are key value pairs
nums
nums.keys() #will return all the keys in dict
nums.values() #will return all the values
#we usually want key-value pairs 
nums.items()#return  a list of tuples with key value pairs 
#we can easily unpack with tuples 
"one" in nums #searching is very fast
#in a new version, 
#dictionaries are sorted by insertion but can't be accessed by index

#list - mutable
#set - mutable
#tuple - immutable
#dictionary - mutable 

my_list = ["h", "e", "l","l","o"]
my_list.append("!")
len(my_list)
my_list[0]
my_list[0:3] 
my_list[:3]
my_list[-1] #very last element
my_list.remove("l") #removes the first instance of l
my_list.insert(2, "l") #position and the element
my_list.pop()
del my_list[0] #recommend not using it
last_item = my_list.pop() 
"!" in my_list
my_list.sort(reverse=True)
sorted(my_list, reverse=True)
type({}) #dictionary
#sets are mutable and no duplicates
my_set = set()
my_set.add(4)
my_set.remove(2)
2 in my_set
my_other = {1,2,3}
my_set.union(my_other)
my_set.difference(my_other)
my_set.intersection(my_other)
#we can't make one item tuple with paranthesis
type((3,))
my_tuple = 1
#tuples are immutable so cant do my_tuple[1] = 2
person = ("Jim", 29, "Austin, TX")
name, age, homeTwon = person
print(names)
print(age)
my_dict = {"key":"value"}
#my_dict[0]: key error, unless key 0 is there because dictionaries don't have orders
my_dict["hello"] = "world"
my_dict["foo"] = "bar"
#to access 
my_dict["hello"]  #key error if hello isnt there
my_dict.get("hello") #lack of an error
my_dict.get("baz", "default")
my_dict.keys()
my_dict.values()
my_dict.items()

#mutability
#lists, dic, sets - mutable
my_list = [1, 2, 3]
my_list[0] = 'a'
my_dict = {"hello": "value"}
my_dict["hello"] = "new value"
my_set = {1,2,3}
#my_set[0] = 'a' #can't do this because it's not in order
my_set.add(a)
#tuples are immutable
my_tuple = (1, 2, 3)
my_tuple[0] #can look up 
#my_tuple[0] = 1 #this will give you an error

#truthiness
True 
False 
type(True)
#this conversion happens under the hood
#bool(True)
bool(0) #false -y 
#any other is truthy including negative numbers
bool([]) #empty sets, lists, tuples, dictionaries are false
#if an item is in it then it's true
bool([1])
bool((1,))
bool({1})
bool({1:1})
bool(None) # none type is fase
#don't name your variable true, false, none
#strings -> sequences 
bool("") #->False
bool("hello") #-> True

3<5
5>3
1<=1
5>=5
#strings compared with ascill values, capital comes before lower 
"T" < "t" #upper case letters are lower valued in ascii 
"bat" < "cat" #but then after upper/lower it works as expected 

1 == 1
#true
"Hello" == "Hello"
#true
[1, 2, 3] == [1, 2, 3]
#true
a= 1
b= 1
a != b
#false 

#is : means identity, stored at the same location?point to the same thing 
#== : equality
x = None
x is None 
x is True 
x is False 
a = [1, 2, 3]
b = [1, 2, 3]
a is b #false, not stored at the same location
a == b # true 

a = None
a is None #true
a is not None  #false 

#and or not
a = True
b = True
a and b
[1] and [2]
#return [2] since [1] is true

a = False
b = True
a and b
#return false 

a = False
b = False 
a and b 
#return false 

[] and {}
#return [] 
[] and {1}
#still return {1}
[1] or [2]
#will return [1]
a = False
b = True
a or b
#return true
[] or [1]
#return [1]
0 or 1
#return 1
not 1
#false 
not 0
#true
if 5:
	print("hello")
print(1 == False)
print(1 == True)
print(0 == False)

#[] or [1]  
#[1]
#[1] or [2]
#[1]
#[] and {} 
#[] 
#[1] and {1}
#{1}
#not []
#True 
#"Hello" and None 
#None 
a = True
b = True
c = True
a and b and c

#for(i = 0; i < 5; i++) {
#	text += "number is" +i +"<br>"; 
#}

colors = ["Red", "Green", "Blue"]
for color in colors:
	print(color)
#the abovie isn't a function, no scope here
print(color) #so still blue
#it's indentation that defines what belongs to for loop
range(5) #implicitly start with 0 and provided number isn't inclusive
#so it gives 0,1,2,3,4 
print(list(range(5)))
for num in range(5):
	print(num)
for num in range(1, 5): #start is inclusive
	print(num)
#range takes 3 arguments and they are positional
for num in range(1, 7, 2):
	print(num)

hex_colors = {"Red":"#FF", "Green":"#008"}
for color in hex_colors:
	print(color) #just the keys 
for label, hex in hex_colors.items(): #list of tuples
	print(label, hex) 
for i, color in enumerate(colors): #return tuple first:index, second:item itself
	print(f"index:{i}, color:{color}")

#a, b, c = (1, 2, 3, 4) too many values un pack error
if 3 <5:
	print("hello")
a = []
if not a:
	print("hello")
b = [1,2]
if b:
	print("hello")
if a:
	print("hello")
else:
	print("good bye")

a = False
b = True
if a:
	print("1")
elif b:
	print("2")
else:
	print("3")

#while loop: that runs forever until some condition is met
#for loop:run untill all items are done
counter = 0
max = 4
while counter < max:
	print(f"the count is: {counter}")
	counter = counter + 1

#to control while loop we can do break, continue, return 
#they control the flow 

#using break
names = ["Nina", "Max", "Rose", "Jimmy"]
for name in names:
	print(f"Hello, {name}")
	if name == "Rose":
		break #won't print jimmy, completely break the loop
for name in names:
	if name != "Rose":
		continue #if not rose, continue back to the loop, when finally rose then print 
	print(f"Hello, {name}")

#two nested for loop, if break is insdie internal one then only the one that's inside breaks
count = 0
while True:
	count += 1
	if count == 5:
		print("count was reached")
		break
def find_target_name(names):
	for name in names:
		print(name)
		if name == "Nina":
			return "Found the special case"
names = ["Max", "Nina", "Rose"]
find_target_name(names) # won't reach rose since we return before reaching it 
'''

#convention for naming python file:lower case
greetings = ["Hello", "Bonjour", "Hola"]
for greeting in greetings:
	print(f"{greeting}, World!")
#to run outside env we have to do 
#python3 hello.py
#usually to debug, use print statement
def mystery():
	num = 10 * 3
	if num == 10:
		print("condition 10")
		num = num * 10
	elif num == 30:
		print("condition 30")
		num = num *30

#we saw how to import local files 
#if we want to use external libraries
#we have to use pip 
#we use pip to request libraries 
#for instance we can do pip3 install requests
#then do import requests in a py file

#using requests import we can interact with apis from python
#apis set of functions/procedures allowing accessing features of a system somewhere else

#client sends request to a server
#server return responds
#to get we use http methods:get/post/put/delete
#generally attach header/body/url parameter along with the requests
#each apis have  different response types
#such as xml, json
#requests turn json response to python dictionaries
#http status codes:
#the ones in 200 ranges success
#500 range: server error 
