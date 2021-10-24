n = 0
while True:
    if n == 1000_000:
        break
    num  = int(f'1{n}2{n}3{n}4{n}5{n}6{n}7{n}8{n}9{n}0')
    root =  num**0.5
    if int(root)**2 == num:
        print(n, int(root), root)
        break
    n += 1
