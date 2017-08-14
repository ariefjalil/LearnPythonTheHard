formatter = "%r %r %r %r" # character format %r returns raw 

print formatter % (1,2,3,4)  #insert value/variables into string
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"I am 6'2\" tall.", #how to combine ' " ?
	"So I said goodnight."
	)
	
	