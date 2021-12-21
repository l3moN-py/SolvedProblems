k, d, n = map(int, input().split())

n = int((n*(n+1))/2)
p = k*n

if d >= p:
    print(0)
else:
    print(p-d)