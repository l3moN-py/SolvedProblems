fib_list = [1,2]
while fib_list[-1] < 4000000:
    fib_list.append(fib_list[-1]+fib_list[-2])

print('Answer:', sum([x for x in fib_list if x%2 == 0]))
