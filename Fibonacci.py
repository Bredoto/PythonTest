import math
def FibonacciGold(n):
    fib = (1.0/math.sqrt(5))*math.pow( (1+ math.sqrt(5))/2,n) - (1.0/math.sqrt(5))*math.pow( (1 - math.sqrt(5))/2,n)
    print fib

def FibonacciSimple(n):
    for i in range(1,20):
        print i

def main():
    for i in range(1,20):
        FibonacciGold(i)
        FibonacciSimple(i)
        
        



main()
