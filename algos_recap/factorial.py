def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    
    return fact

def recursive_factorial(n):

    if n == 1 or n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(iterative_factorial(5))
print(recursive_factorial(5))
