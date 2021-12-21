import re

lucky_nums = [i for i in range(1,1001) if re.match(r'^[4,7]+$',str(i))]
# print(lucky_nums)
num = int(input())

for lucky_num in lucky_nums:
    if num%lucky_num == 0:
        print('YES')
        break
else:
    print('NO')