res = 0
for i in range(2,5*9**5):
    if i == sum([int(str(i)[a])**5 for a in range(len(str(i)))]):
        res += i
print('Result:', res)
