
inp = [0,6,0,5,0,8,0,6]

x = [(a, inp[a]) for a in range(8)]
print(x)

print(sorted(x, key=lambda x: x[1], reverse=True)[0][0])
