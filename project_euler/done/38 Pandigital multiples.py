n = 1
res = []
def pandigital(num):
    for i in range(1,10):
        if str(i) not in num:
            return False
    return True
def do(num):
    x = ''
    c = 1
    while len(x) < 9:
        x += str(num*c)
        c += 1
    if len(x) == 9:
        if pandigital(x):
            res.append(int(x))


while n < 100000:
    do(n)
    n += 1

print(len(res), res)
print('Answer:', max(res))
