def foo(num):
    for div in range(3,num + 1,2):
        if num % div == 0:
            return [div, num // div]
num = 600851475143
res = []
while True:
    if foo(num) == None:
        break
    res.append(foo(num)[0])
    num = foo(num)[1]
print('Answer:', sorted(res, reverse = True)[0])
