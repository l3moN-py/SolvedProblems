def pentagon(n):
    x = (1 + (1-4*3*(-2*n))**0.5)/6
    if x == int(x):
        return True
    return False

l = []
n = 1
t = True
while t:
    l.append(int(n*(3*n-1)/2))
    for i in range(len(l)-1):
        if pentagon(l[-1]-l[i]) and pentagon(l[-1]+l[i]):
            print('Answer:', l[-1]-l[i])
            t = False
    n += 1
