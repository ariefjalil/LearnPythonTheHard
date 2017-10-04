print "Let's practice everything."
print 'you\'d need to know \'bout ecscapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor passion from intuition
and requires and explnation
\n\t\twhere there is none.
"""

print "--------"
print poem
print "--------"

five = 10 - 2 + 3 - 6
print "this should be five: %s" %five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans, jars, crates

start_point = 1000
cock, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (cock, jars, crates)

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
