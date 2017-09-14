def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a + b #Return gives something back or replies to the caller function

def subtract (a,b):
    print "Subtracting %d - %d" %(a,b)
    return a-b

def multiply(a,b):
    print "Multiplying %d * %d" % (a,b)
    return a*b

def divide(a,b):
    print "Dividing %d / %d" %(a,b)
    return a/b

def plusminus(a,b,c):
    print "plus minus %d + %d - %d" %(a,b,c)
    return a+b-c

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide (100,2)
stamina =plusminus(20,10,5)

print "Age: %d, Height: %d, Weight: %d, IQ: %d, Stamina: %d" % (age, height, weight, iq,stamina)

# A puzzle for extra credit.

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

what2 = age + height -weight*iq/2 #extra credit

print "That becomes: ", what, "Can you do it by hand?"
print "Value is", what2, "okay"
