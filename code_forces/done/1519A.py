for _ in range(int(input())):
    r, b, d = map(int, input().split())
    d += 1
    if min(r,b)*d >= max(r,b):
        print('YES')
    else:
        print('NO')