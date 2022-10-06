#!/usr/bin/python3
import sys 
import urllib.parse
import urllib.request
import os
import platform

print("XDG started python script")
print("Arguments: " , str(sys.argv))

protocol=''
parameters = ''
[protocol,parameters] = sys.argv[1].split(':',1)

commandParts = parameters.split('&')
options = {} 
for part in commandParts:
	splitPart = part.split('=')
	key = splitPart[0]
	value = splitPart[1]
	print("Key %s has value %s" %(key,value))
	options[key]=value

labelSize = 'pt36'
if options['labelWidth']:
	labelSize = 'pt'+options['labelWidth']	

decodedUrl = urllib.parse.unquote(options['url'])

try:
	os.mkdir('/tmp/thingsToPrint/')
except OSError as error:
    print(error)    

tempFilename = '/tmp/thingsToPrint/' + options['name'] + '.png'

print("fetching: "+decodedUrl)

urllib.request.urlretrieve(decodedUrl, tempFilename)

commandString = 'python3 /home/pi/brother_ql/brother_ql/cli.py '

if platform.system() == 'Darwin' : 
    commandString +=  "-b network -m PT-P900W -p tcp://192.168.86.52 print -c --no-cut -l " + labelSize 
else :
    commandString +=  "-b linux_kernel -m PT-P900W  -p /dev/usb/lp0 print -c --no-cut -l " + labelSize 

quantityToPrint = 1 
if options['quantity'].isnumeric():   
    quantityToPrint = int(options['quantity'])

for _ in range(quantityToPrint): 
    commandString += ' ' + tempFilename

print("executing command "+ commandString)
stream = os.popen(commandString)
output = stream.read()
print(output)

