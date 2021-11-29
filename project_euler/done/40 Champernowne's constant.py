i = 0
result = 1
d = ''

while len(d) < 1000001:
    d += str(i)
    i += 1

for x in [int(d[a]) for a in [1,10,100,1000,10000,100000,1000000]]:
    result *= x
print('Answer:', result)
