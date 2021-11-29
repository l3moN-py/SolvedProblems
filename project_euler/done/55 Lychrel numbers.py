
def palindrome(num):
    return str(num) == str(num)[::-1]

lycher = 0
for num in range(10000):
    num += int(str(num)[::-1]) #Surprisingly, there are palindromic numbers that are themselves Lychrel numbers.
    for test in range(50):
        if palindrome(num):
            break
        if test == 49:
            lycher += 1
            break
        if not palindrome(num):
            num += int(str(num)[::-1])

print('Result:', lycher)
