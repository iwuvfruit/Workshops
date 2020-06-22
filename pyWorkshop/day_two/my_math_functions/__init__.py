def add_numbers(x, y):
	return x+y

#now I can do from my_math_functions import add_numbers
#sometimes it's good to do import my_math_functions 
#and then my_math_functions.add_numbers(5, 3)

my_dict = {num:num*num for num in range(30)}
print(my_dict) #hard to read, I can use a library
from pprint import pprint
pprint(my_dict)
from pprint import pprint as pp 
pp(my_dict)

#we can go to pypi to see the libraries/packages
#be in your virtual env 
#python3 -m pip install requests  
