from operator import xor

num1, num2 = input(), input()
l = len(num1)

result = bin(xor(int(num1, 2), int(num2, 2)))

print(result[2:].zfill(l))
