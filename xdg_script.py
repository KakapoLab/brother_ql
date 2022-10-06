#!/usr/bin/python3
import sys 
print("XDG started python script")
print("Arguments: " , str(sys.argv))

commandParts = sys.argv[1].split('&')
options = {} 
for part in commandParts:
	splitPart = part.split('=')
	key = splitPart[0]
	value = splitPart[1]
	print("Key %s has value %s" %(key,value))
	options[key]=value

# get file to print from URL and save in local folder

# execute print command

