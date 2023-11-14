# Нельзя повторять предыдущее действие

from functools import lru_cache

def move(n, r):
    if r == '+1':
        return (n + 2, '+2'), (n * 2, '*2')
    if r == '+2':
        return (n + 1, '+1'), (n * 2, '*2')
    if r == '*2':
        return (n + 1, '+1'), (n + 2, '+2')
    else:
        return (n + 1, '+1'), (n + 2, '+2'), (n * 2, '*2')

@lru_cache(None)
def game(n, r):
    if n >= 34:
        return 'w'
    if any(game(x, sing) == 'w' for x, sing in move(n, r)):
        return 'p1'
    if all(game(x, sing) == 'p1' for x, sing in move(n, r)):
        return 'v1'
    if any(game(x, sing) == 'v1' for x, sing in move(n, r)):
        return 'p2'
    if all(game(x, sing) == 'p1' or game(x, sing) == 'p2' for x, sing in move(n, r)):
        return 'v2'

for i in range(1, 33):
    print(i, game(i, ''))