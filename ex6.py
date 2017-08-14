x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
z = "brown"
print x
print y

#this is where python format character being insert in a string.
print " I said: %r." %x
print " I also said: '%s' ." %y
print " I also said %s without quote." %z # %s takes the string without double quote
print " This time I said %r with quote." %z  # %r format characters its like saying "print this anyway"


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %s"

print joke_evaluation % hilarious

w = "This is the left side of...."
e = "a string with a right side."

print w + e 