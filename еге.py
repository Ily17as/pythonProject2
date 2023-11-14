import turtle
from functools import lru_cache
from math import ceil
from fnmatch import fnmatch
from sys import setrecursionlimit

f = open('27.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
summa = 0
maxi = 0
for i in range(n):
    maxi = max(maxi, a[i])
    if i + k < len(a):
        summa = max(summa, maxi+a[i+k])
print(summa)

