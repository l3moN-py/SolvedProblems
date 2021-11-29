from collections import Counter

a = 1
s = 1000
res = []
while True:
    for b in range(1,int((a**2-(s-a)**2)/(-2*(s-a))) + 1):
        c = (a**2 + b**2)**0.5
        if c == int(c) and a+b+c <= 1000:
            res.append(a+b+int(c))
    a += 1
    if a == s//2:
        break
#print(res)
print('Answer:', Counter(res).most_common()[0])
