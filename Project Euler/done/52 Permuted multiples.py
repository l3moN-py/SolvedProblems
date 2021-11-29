num = 1
while True:
    x = sorted([_ for _ in str(num)])
    x2 = sorted([_ for _ in str(num*2)])
    x3 = sorted([_ for _ in str(num*3)])
    x4 = sorted([_ for _ in str(num*4)])
    x5 = sorted([_ for _ in str(num*5)])
    x6 = sorted([_ for _ in str(num*6)])
    if x == x2 == x3 == x4 == x5 == x6:
        print('Result:', num)
        break
    num += 1
