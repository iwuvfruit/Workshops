class Vehicle:

	#this is more of implementation detail
	#number_of_wheels = 4

	def __init__(self, make, model, fuel="gas"):
		self.make = make
		self.model = model
		self.fuel = fuel

	def __str__(self):
		return f"I drive {self.make} {self.model} it runs on {self.fuel}"

daily = Vehicle("Subaru", "Crosstrek")
print(daily)
#we see <__main__.Vehicle object at 0x01230FD0>
#__main__:gets runned directly 
print(f"I drive {daily.make} {daily.model} it runs on {daily.fuel}")

print("for Class", Vehicle.number_of_wheels)
print("Instance",  daily.number_of_wheels)

daily.number_of_wheels = 3
print("for Class", Vehicle.number_of_wheels)
print("Instance",  daily.number_of_wheels) #now for this instance the number of wheels is 3

#inherits from vehicle
class Car(Vehicle):
	
	number_of_wheels = 4
	#if I don't provide init method for subclass,
	#it will use init method from vehicle 

class Truck(Vehicle):
	number_of_wheels = 6

	def__init__(self, make, model, fuel = "diesel"):
		super().__init__(make, model, fuel) #I'm calling init because I need to overwrite fuel  


#making class for the final excercsie did for the first day

class GitHubRepo:
	def __init__(self, name, language, num_stars):
		self.name = name
		self.language =language
		self.num_stars = num_stars

	def __str__(self):
		return f"-> {self.name} with {self.language} has {self.num_stars}"

vue = GitHubRepo(name = "vue", ,language="Javascript", num_stars=50000)
#this return what repr returns, repr(vue)
print(vue) #under the hood, this uses str because we want to show human readable one with print 

