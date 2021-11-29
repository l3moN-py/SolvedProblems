n = 1001
n = n//2 + 1
res = [1]
for i in range(n):
    for _ in range(4):
        res.append(res[-1] + 2*i)
del res[:4]
print('Answer:', sum(res))
