#putting a lot of exceptions into custom module
class GitHubApiError(Exceptions): #exceptions for the base class
	def __init__(self, status_code):
		if status_code == 403:
			message = "rate limit reached"
		else: 
			message = f"status code was: {status_code}"

		super().__init__(message) #passing message to exception

#now if I do raise GitHubApiError(403), the message shows up 

#common errors:
#indentation error
#syntax error ex)[1, 2 3]
#zero division error  
#type error ex) 2 + "3"
#ValueError ex) int("A")
#keyError ex)wrong key in dictionary
#class MyError(Exception):
#	pass
#raise MyError() //this generates traceback
class MyError(Exception):
	def __init__(self, message):
		new_message = f"{{message}}"
 		super().__init__(message)
 raise MyError("need to provide message")

 my_dict = {"Hello":"Value"}
 try:
 	print(my_dict["random key"])
 except KeyError:
 	print("no key found")

 try:
 	my_dict["random key"]
 except KeyError as e:
 	print(f"oh no! error is {e}")

list(range(5, -1, -1))
for num in ranges(5, -1, -1):
	try:
		5 / num
	except ZeroDivisionError:
		raise MyError("don't divide by error")


