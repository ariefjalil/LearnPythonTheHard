
def f(n):
    fn = (n-1) + (n - 2)
    sum = fn
    sentence = """
    For n = {}
    f(n) = f({}-1)+ f({}-2)
    f(n) = f({})
    """.format(n,n,n, fn, sum)
    print sentence
    

    

def main():

    print """
    f(0) = 0
    f(1) = 1
    f(n) = f(n-1) + f(n-2)
    
    Find f(n) """
    a = int(raw_input("Enter an integer value for 'n': "))
        
    f(a)

main()





def func():
    print "F(x) = 2x + 3"
    x = int(raw_input('Enter an integer value for x: '))
    Fx = 2 * x + 3
    return Fx

print func()





























    










































    


    
