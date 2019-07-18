fib = lambda n : n if n <= 2 else fib(n-1) + fib(n-2)
print(fib(6))
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)
print(fib(6))