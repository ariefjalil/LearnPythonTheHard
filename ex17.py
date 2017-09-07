# Copy one file to another

from sys import argv
from os.path import exists #returns True if a file exists. False if not. 

script, from_file, to_file = argv

#Opening a file from defined argv.
print "Opening the file %s....." %from_file
target = open(from_file, 'w') #'w' creates a file if it doesnt exits, empties if it does

print"Now I'm going to ask you to write these to the file."
line1 = raw_input("Line 1: ")
print" I'm going to write these to the file."

target.write(line1)
target.close() # .close() acts as "SAVE file"

print "Copying from %s to %s" %(from_file, to_file)

#We could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print " The input file is %d bytes long. Output file exists? %r" % (len(indata), exists(to_file))

#print "Does the output file exists? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input(">")

#copying file to another
output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

#output.close() #Save whatever written to output file and exit.
input.close()


