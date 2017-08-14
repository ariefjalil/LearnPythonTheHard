
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: %s " %days #can unse either character format or var to get string.
print "Here are the days:", days

print "Here are the months: ", months
print "Here are the months:%s" %months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#W What is the function of three double quotes?

# Triple quote is an escape sequence to tell python that the " inside the string isnt a real double quote
#e.g

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'