def f(n, r):
    if n == r:
        return 1
    elif n > r or n == 10:
        return 0
    if n < r:
        if n == 1:
            return f(n + 1, r) + f(n + n + 1, r)
        else:
            return f(n + 1, r) + f(n + n + 1, r) + f(n + n - 1, r)

for i in range(1, 29):
    print(f(1, i), end=' ')