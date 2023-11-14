import turtle
from functools import lru_cache
from math import ceil
from fnmatch import fnmatch
from sys import setrecursionlimit

f = open('24.txt', 'r')
s = f.readline().strip()

a = [0 for i in range(26)]
s = s.replace('A', ' 0 ')
s = s.replace('B', ' 1 ')
s = s.replace('C', ' 2 ')
s = s.replace('D', ' 3 ')
s = s.replace('E', ' 4 ')
s = s.replace('F', ' 5 ')
s = s.replace('G', ' 6 ')
s = s.replace('H', ' 7 ')
s = s.replace('I', ' 8 ')
s = s.replace('J', ' 9 ')
s = s.replace('K', ' 10 ')
s = s.replace('L', ' 11 ')
s = s.replace('M', ' 12 ')
s = s.replace('N', ' 13 ')
s = s.replace('O', ' 14 ')
s = s.replace('P', ' 15 ')
s = s.replace('Q', ' 16 ')
s = s.replace('R', ' 17 ')
s = s.replace('S', ' 18 ')
s = s.replace('T', ' 19 ')
s = s.replace('U', ' 20 ')
s = s.replace('V', ' 21 ')
s = s.replace('W', ' 22 ')
s = s.replace('X', ' 23 ')
s = s.replace('Y', ' 24 ')
s = s.replace('Z', ' 25 ')
s = s.split()

for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        a[int(s[i + 1])] += 1
print(a)
print(a.index(max(a)))
