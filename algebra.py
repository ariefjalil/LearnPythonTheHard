def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum {} and {} is {}.'.format(x, y, sum)
    print sentence
    print " The sum %r and %r is %r." % (x, y, sum)
    

    
def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 53590248291058)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a,b)

main()

