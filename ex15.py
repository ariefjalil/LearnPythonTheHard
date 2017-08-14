#pass variable to script 
from sys import argv 

script, filename = argv

#call a function on txt to open (filename)

txt = open(filename)

print "Here's your file %r: " %filename
#give command to file by using dot .
print txt.read() #Hey txt, do your read command with no parameter!
txt.close()

file_again = raw_input ("Please type any filename")
txt_again = open(file_again)
print txt_again.read()	

txt_again.close()




