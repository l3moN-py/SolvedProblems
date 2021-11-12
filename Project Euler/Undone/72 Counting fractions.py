# n/d
frac = []
for d in range(2,9_000):
    for n in range(1, d):
        frac.append((n/d).as_integer_ratio())

print(frac)