def Birthday(person): #function
    print """
    Happy birthday to you,
    Happy birthday to you,
    Happy birthday to, {}
    Happy birthday to you. """.format(person)



def main():
#last two lines are outside of definitons

    person = raw_input("Whose birthday is it today?: ")
    Birthday(person)

main()
