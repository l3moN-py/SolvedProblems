n = 0
while True:
    n_sq = n*(3*n-2)
    if 1000 < n_sq < 10_000:
        print(n)
    elif n > 10_000:
        break
    n += 1