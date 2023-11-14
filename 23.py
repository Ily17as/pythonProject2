def f(n, r):
    if n == r:
        return 1
    elif n > r or n == 23:
        return 0
    else:
        return f(n + 1, r) + f(n * 2, r)
print(f(1, 21))