num, k = map(int, input().split())

for _ in range(k):
    if str(num)[-1] != '0':
        num -= 1
    else:
        num //= 10

print(num)