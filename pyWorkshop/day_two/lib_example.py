import os #operating system function

my_folder = os.getcwd() #getting current working directory
print(f"Here are the files in: {my_folder}:")
with os.scandir(my_folder) as folder:
	#context manager will do the clean up using with os.scandir
	for entry in folder:
		print(f"-{entry.name}")

