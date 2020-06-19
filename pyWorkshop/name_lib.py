def upper_case_name(name):
	return name.upper()

#if dunder name is main then run this 
if  __name__ == "__main__":
	name = "Nina"
	up_case_name = upper_case_name(name)
	print(f"upper case name  is {up_case_name}")
	print("dunder name", __name__) #main!!
#now in other py file I only see their contents
