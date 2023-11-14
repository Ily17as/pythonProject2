
from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1500)

def move(n):
    n1, n2 = n
    return (n1 + 1, n2), (n1 * 2, n2), (n1, n2 + 1), (n1, n2 * 2)

@lru_cache(None)
def game(n):
    if sum(n) >= 77:
        return 'w'
    if any(game(kol) == 'w' for kol in move(n)):
        return 'p1'
    if all(game(kol) == 'p1' for kol in move(n)):
        return 'v1'
    if any(game(kol) == 'v1' for kol in move(n)):
        return 'p2'
    if any(game(kol) == 'p1' or game(kol) == 'p2' for kol in move(n)):
        return 'v2'



for i in range(1, 68):
   if game((8, i)) == 'v1':
       print(i)