x = []
def d(n):
    global Sum
    Sum = 0
    for i in range(1,n):
        if n%i == 0:
            Sum += i
    return Sum

for f in range(1,10001):
    d(f)
    j = d(Sum)
    if f == j:
        if str(f) != str(d(Sum)):
            x.append(f)


print(x)
print(sum(x))
