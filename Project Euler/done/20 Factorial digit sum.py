n = 100
y = 1
for i in range(1, n+1):
    y *= i
h = 0
for x in str(y):
    h += int(x)

print(h)
