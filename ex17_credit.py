from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Opening file %s" %from_file

target =open(from_file, 'w')

print "Now I'm going to ask you to write."
line1 = raw_input("Line 1: ")
print "Writing these to the file."

target.write(line1)
target.close()

print "Copying from %s to %s" % (from_file, to_file)
x = open(from_file)
indata = x.read()

print "The input file is %d byte long" %len(indata)

print "Does the out file exists? %r" %exists(to_file)
print "Ready, hit RETURN to continue."
raw_input (">")

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."


output.close()
x.close()
