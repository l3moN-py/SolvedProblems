x = 0

for num_of_op in range(int(input())):
    operation = input()
    if '-' in operation:
        x -= 1
    else:
        x += 1

print(x)