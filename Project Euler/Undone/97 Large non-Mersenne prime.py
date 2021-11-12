def get_sq_short(sq):
    n = 2
    for i in range(sq-1):
        n = int(str(n)[-10:])*2
    return str(n)[-10:]

num = 7_830_457

print(str(int(get_sq_short(num))*28433+1)[-10:])
