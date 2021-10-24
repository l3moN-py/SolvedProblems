import itertools
count = 0
for num in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    if count == 1000000 - 1:
        res = list(num)
        break
    count += 1
#print(res)
print(''.join(str(x) for x in res))
