import turtle
from functools import lru_cache
from math import ceil
from math import sqrt
from fnmatch import fnmatch
from sys import setrecursionlimit
from math import ceil

f = open('Новый текстовый документ.txt', 'r')
a = f.readline().strip()
# a = a.replace('A', ' 1 ')
# a = a.replace('B', ' 2 ')
# a = a.replace('C', ' 3 ')
# a = a.replace('D', ' 4 ')
# a = a.replace('E', ' 5 ')
# a = a.replace('F', ' 6 ')
# a = a.replace('G', ' 7 ')
# a = a.replace('H', ' 8 ')
# a = a.replace('I', ' 9 ')
# a = a.replace('J', ' 10 ')
# a = a.replace('K', ' 11 ')
# a = a.replace('L', ' 12 ')
# a = a.replace('M', ' 13 ')
# a = a.replace('N', ' 14 ')
# a = a.replace('O', ' 15 ')
# a = a.replace('P', ' 16 ')
# a = a.replace('Q', ' 17 ')
# a = a.replace('R', ' 18 ')
# a = a.replace('S', ' 19 ')
# a = a.replace('T', ' 20 ')
# a = a.replace('U', ' 21 ')
# a = a.replace('V', ' 22 ')
# a = a.replace('W', ' 23 ')
# a = a.replace('X', ' 24 ')
# a = a.replace('Y', ' 25 ')
# a = a.replace('Z', ' 26 ')
# a = a.split()

n = ''
mx = 0
k = 0

for i in range(len(a) - 1):
    if a[i] <= a[i + 1]:
        k += 1
    else:
        if mx < k:
            n = a[i - k] + ' ' + a[i]
            mx = k
        k = 0
print(a)
print(mx + 1, n)
