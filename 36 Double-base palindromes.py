x = []
y = []
l = []
last = []

def dtb(num):
    if num > 1:
        dtb(num // 2)
    y.append(str(num%2))

for i in range(1, 1000001):
    if str(i) == str(i)[::-1]:
        l = []
        y = []
        dtb(i)
        l = ''.join(y)
        if str(l) == str(l)[::-1]:
            last.append(i)


print(last)
print(sum(last))
