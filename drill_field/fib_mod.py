# Fibonacci series practice
fib_start = 0

def fib(n):
    a, b, count = fib_start, 1, 0
    while count < n:
        print(a, end=' ')
        a, b = b, a+b
        count += 1
    print()

def fib_under(n):
    a, b = fib_start, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

