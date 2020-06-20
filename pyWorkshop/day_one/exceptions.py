#this will throw an error
try:
	int("a")
#we have to put the exact right exception class
except ValueError as e:
	print("opps you cant do this")
	print(e)
print("this is the end of my progrma")