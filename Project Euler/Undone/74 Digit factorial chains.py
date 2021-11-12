from math import factorial
from functools import cache

F = {x:factorial(x) for x in range(10)}

# def chains(num):
#     mem = []
#     for n in range(17):
#         if num in mem:
#             return 0
#         mem.append(num)
#         num = sum([F.get(int(d)) for d in str(num)])
#     else:
#         if num in mem:
#             return 1
#     return 0
#
# count = 0
# for x in range(1_000):
#     if chains(x):
#         count += 1
#
# print(count)

def chain(x):
    pass

for x in range(1_000):
    if chain(x):
        print(x)
