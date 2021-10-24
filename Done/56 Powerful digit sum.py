res = 0

for a in range(100):
    for b in range(100):
        r = sum([int(a) for a in str(a**b)])
        if r > res:
            res = r
print(res)
