a = 190

def factorial(n):
    f = 1
    while n >= 1:
        f = f * n
        n = n - 1
    return f

answer = factorial(a)
print(a)
print(answer)
