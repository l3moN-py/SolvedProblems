num = 100
x = []
y = 0
for i in range(1, num + 1):
    x.append(i*i)
    y += i

print('Answer:', y*y-sum(x))
