import sys

#arguments = sys.argv #0th-file name in string 
arguments =  sys.argv[1:] #we don't really care about the file name
print(f"we received these arguments:{arguments}")

print(f"we are currently running on a {sys.platform} machine")


#ran python3 sys_example.py 123 hello good bye