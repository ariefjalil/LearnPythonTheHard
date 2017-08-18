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

#----------------------------------------------

def happyBirthdayEmily():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")

def happyBirthdayAndre():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Andre.")
    print("Happy Birthday to you!")

def main():
    happyBirthdayEmily()
    happyBirthdayAndre()
main()

#--------------------------------------------------
# function with parameter
def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

happyBirthday('Emily')
happyBirthday('Raju')

#--------------------------------------------------
#function in parameter called in main()

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    happyBirthday('Emily')
    happyBirthday('Mustafa')

main()
