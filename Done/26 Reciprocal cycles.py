def whole(r, n):
    return r // n
def rest(r, n):
    return r % n
def foo(num):
    w = [whole(1, num)]
    r = [rest(1, num)]
    #return w,r
    while True:
        f = rest(r[-1]*10, num)
        if f in r:
            return (len(r) - r.index(f), num)
        elif f == 0:
            return (0,0)
        else:
            r.append(f)

print('Answer:',sorted([foo(a) for a in range(2,1001)], reverse = True)[0][1])
