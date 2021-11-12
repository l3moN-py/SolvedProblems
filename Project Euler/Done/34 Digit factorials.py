import math

b = 1
while b*math.factorial(9) > int('9'*b):
    b += 1
b = b*math.factorial(9)

x = []

for i in range(3,b):
    dlzka = len(str(i))
    k = 0
    for l in range(dlzka):
        k += math.factorial(int(str(i)[l]))
    if k == i:
        x.append(i)
        
print(x)         
print(sum(x))



