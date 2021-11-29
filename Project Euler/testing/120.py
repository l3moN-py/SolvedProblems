a = 13

for n in range(1,30):
    num = (a-1)**n + (a+1)**n
    print(n, num, num%(a**2))