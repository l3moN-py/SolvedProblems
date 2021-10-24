x = []
y = 100
for a in range(2,y + 1):
    for b in range(2,y + 1):
        x.append(a**b)

#print(sorted(set(x)))
print(len(sorted(set(x))))
