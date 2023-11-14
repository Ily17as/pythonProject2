import turtle
from functools import lru_cache
from math import ceil
from math import sqrt
from fnmatch import fnmatch
from sys import setrecursionlimit
from math import ceil

f = open('Новый текстовый документ.txt', 'r')
n, k = map(int, f.readline().split())
a = [int(x) for x in f]

a = sorted(a, reverse=True)
counter = 0
mx1 = 0
for i in range(len(a)):
    if 220 >= a[i] >= 200:
        mx1 = max(a[i], mx1)
        counter += 1
        k -= a[i]

a = sorted(a)
mx2 = 0
for i in range(len(a)):
    if (a[i] > 220) or (a[i] < 200):
        if k - a[i] >= 0:
            counter += 1
            k -= a[i]
        else:
            k += a[i - 1]
            for j in range(i, len(a)):
                if k - a[j] < 0:
                    mx2 = a[j - 1]
                    break
            break
print(a)
print(k)
print(mx1)
print(mx2)
print(counter, max(mx1, mx2))
