my_name = 'Arief Jalil'
my_age = 33 
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
inch = 2.54 #centimeter

my_cm_height = my_height * 2.54

print "Let's talk about Mr %s." % my_name
print "He's %d inches tall." %my_height
print "My height in CM is %d cm" %my_cm_height
print "He's %d pound heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)

