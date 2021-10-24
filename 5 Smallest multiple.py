x = 2
def isDiv(num):
    for i in range(3,21):
        if num%i != 0:
            return False
    return True

while isDiv(x) == False:
    x += 2

print('Answer:', x)
 