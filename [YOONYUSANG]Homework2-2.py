def factorial(n):
    rst = 1
    for _ in range(n):
        rst=rst*(n-_)
    return rst

n=int(input('Enter a number: '))
print(factorial(n))