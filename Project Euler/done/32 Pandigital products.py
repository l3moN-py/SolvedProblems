def req(num):
    for i in range(len(str(num))):
        if str(num).count(str(num)[i]) > 1:
            return False
    return True
def not_same(a, b):
    for a in list(str(a)):
        if a in str(b):
            return False
    return True
def pandigital(num):
    if len(num) != 9:
        return False
    for i in range(1,10):
        if str(i) not in str(num):
            return False
    return True
res = []
for a in range(100):
    if a%10 != 0 and req(a):
        for b in range(10000):
            if len(str(b*a)) + len(str(a)) + len(str(b)) > 9:
                break
            if b%10 != 0 and req(a) and not_same(a, b):
                product = a*b
                if req(product) and not_same(str(a)+str(b), product) and pandigital(str(a)+str(b)+str(product)):
                    res.append(product)
print('Answer:', sum(set(res)))
