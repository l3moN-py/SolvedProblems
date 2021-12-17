import result as result


def skrzat(base, number):
    result = 0
    if base == 'b':
        for i in range(len(number)):
            result += int(number[::-1][i])*(2**i)*(-1)**i

    return result

# print(skrzat('b', '0111111'))

def dec_to_bin(number):
    result, i = [], 1 if number <= 0 else 0
    while True:
        if number == 0:
            return result
        result.append(number % 2)
        # number = number//2
        number = number//(2*(-1)**i)
        i += 1

print(dec_to_bin(-137)[::-1])
