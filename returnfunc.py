#f(0) = 0

#f(1) = 1

#f(n) = f(n-1) + f(n-2)

def f(n):
    sum = (n-1) + (n - 2)
    sentence = """
    For F({}) = f({}-1)+ f({}-2) is {}
    """.format(n,n,n, sum)
    print sentence

def main():

    print """
    f(0) = 0
    f(1) = 1
    f(n) = f(n-1) + f(n-2)
    Find f(n) """
    a = int(raw_input("Enter an integer for 'n': "))
    f(a)

main()
