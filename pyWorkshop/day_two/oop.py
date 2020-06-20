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
dict(zip(players, scores))



