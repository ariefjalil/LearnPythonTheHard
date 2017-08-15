def sumProblem(x, y):
    sum = x + y
    #sentence = 'The sum {} and {} is {}.'.format(x, y, sum)
    #print sentence
    print " The sum %r and %r is %r." % (x, y, sum)
    

    
def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 53590248291058)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))


#anything given to raw_input is return as string. e.g c =4, d=3 = '43' and not 7
    c = raw_input("enter an integer:")
    d = raw_input ("enter an integer again:")
    sumProblem(a,b)
    sumProblem(c,d)
    

main()

