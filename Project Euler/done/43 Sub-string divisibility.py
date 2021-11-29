def pandigital(num):
    for t in range(10):
        if str(t) not in str(num):
            return False
    return True
res = 0
while True:
    for a in range(1,10):
        for b in range(10):
            num = str(a)
            if str(b) not in num:
                num += str(b)
                for c in range(10):
                    num = str(a)+str(b)
                    if str(c) not in num:
                        num += str(c)
                        for d in range(0,10,2):
                            num = str(a)+str(b)+str(c)
                            if str(d) not in num:
                                num += str(d)
                                for e in range(10):
                                    num = str(a)+str(b)+str(c)+str(d)
                                    if str(e) not in num and (c+d+e)%3 == 0:
                                        num += str(e)
                                        for f in range(0,10,5):
                                            num = str(a)+str(b)+str(c)+str(d)+str(e)
                                            if str(f) not in num:
                                                num += str(f)
                                                for g in range(10):
                                                    num = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                                                    if str(g) not in num and (int(str(e)+str(f)+str(g)))%7 == 0:
                                                        num += str(g)
                                                        for h in range(10):
                                                            num = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
                                                            if str(h) not in num and (int(str(f)+str(g)+str(h)))%11 == 0:
                                                                num += str(h)
                                                                for i in range(10):
                                                                    num = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
                                                                    if str(i) not in num and (int(str(g)+str(h)+str(i)))%13 == 0:
                                                                        num += str(i)
                                                                        for j in range(10):
                                                                            num = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)
                                                                            if str(j) not in num and (int(str(h)+str(i)+str(j)))%17 == 0:
                                                                                num += str(j)
                                                                                res += int(num)
    break

print('Answer:', res)

#Other solution (not mine)

#from itertools import permutations
#print(sum(int(''.join(x)) for x in permutations('0123456789', 10) if all([not int(''.join(x)[n[0]:n[1]]) % n[2] for n in [(1, 4, 2), (2, 5, 3), (3, 6, 5), (4, 7, 7), (5, 8, 11), (6, 9, 13), (7, 10, 17)][:7]])))
