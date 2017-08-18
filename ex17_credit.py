# Copy one file to another

from sys import argv
from os.path import exists #returns True if a file exists. False if not. 

script, from_file, to_file = argv


input = open(from_file)
indata = input.read()
raw_input(">")

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close() #Save whatever written to output file and exit.
input.close()


