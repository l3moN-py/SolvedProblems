def test():
    divisors = 500
    num = 0
    i = 1
    while True:
        num = num + i
        if len([a for a in range(1,int(num**0.5)+1) if num%a == 0])*2 > divisors:
            return num
        i += 1
print(test())
