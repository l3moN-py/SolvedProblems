for a in range(1, 999):
    for b in range(a, 1000):
        c = (a**2 + b**2)**0.5
        if a + b + c == 1000:
            if c == int(c):
                print('Answer:', int(a * b * c))
