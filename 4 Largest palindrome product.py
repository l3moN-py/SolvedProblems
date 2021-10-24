new_list = []
for i in range(100,1000):
    for x in range(100,1000):
        multiply = i * x
        if str(multiply) == str(multiply)[::-1]:
            #print(multiply)
            new_list.append(multiply)

new_list.sort()
print('Answer:', new_list[::-1][0])
