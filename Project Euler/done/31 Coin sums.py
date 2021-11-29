new_list = []
for a in range(0,201,200):
    for b in range(0,201-a,100):
        for c in range(0,201-b,50):
            for d in range(0,201-c,20):
                for e in range(0,201-d,10):
                    for f in range(0,201-e,5):
                        for g in range(0,201-f,2):
                            for h in range(0,201-g,1):
                                if a+b+c+d+e+f+g+h == 200:
                                    new_list.append((a,b,c,d,e,f,g,h))
#print('200, 100, 50, 20, 10, 5, 2, 1')
print(new_list)
print('')
print(len(new_list))
