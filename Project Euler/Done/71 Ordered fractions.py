num=0
def get_fraction(den):
    global num
    while True:
        if num/den >= 3/7 or den < num:
            return (num-1, den-1)
        num += 1

frac = []
for i in range(2,1_000_000):
    frac.append(get_fraction(i))

print(sorted(list(filter(lambda x: (x[0]/x[1])<3/7, set(frac))), key=lambda x: x[0]/x[1], reverse=True)[0])

