def div_water(num):
    if num%2 == 0 and num != 2:
        return 'YES'
    return 'NO'

print(div_water(int(input())))