lucky_nums =[4,7,]

num = input()

if (num.count('4') + num.count('7')) in lucky_nums:
    print('YES')
else:
    print('NO')