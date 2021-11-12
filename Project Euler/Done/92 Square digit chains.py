from functools import cache

@cache
def foo(n):
    if n == '89':
        return True
    elif n == '1':
        return False
    return foo(str(sum(map(int, map(lambda x: int(x)**2, n)))))

x = 10_000_000
def with_cache(count = 0):
    for n in range(1,x):
        if foo(str(n)):
            count += 1
    return count

print(with_cache())
