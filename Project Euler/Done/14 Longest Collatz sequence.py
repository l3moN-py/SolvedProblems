'''
num = int(837799)
new_list = [num,]
new_list2 = []
while True:
    if int(num) == 1:
        if len(new_list) > len(new_list2):
            new_list2 = new_list
        break
    elif num%2 == 0:
        num = num/2
        new_list.append(int(num))
    elif num%2 == 1:
        num = num*3 + 1
        new_list.append(int(num))
    
    
print(new_list)
print(len(new_list))
print(new_list2)
'''

new_list2 = []
for i in range(1,1000000):
    num = int(i)
    new_list = [num,]

    while num != 0:
        if int(num) == 1:
            if len(new_list) > len(new_list2):
                new_list2 = new_list
                #print('s')
            break
        elif num%2 == 0:
            num = num/2
            new_list.append(int(num))
        elif num%2 == 1:
            num = num*3 + 1
            new_list.append(int(num))
            
#print(new_list)
#print('')
#print(len(new_list))
#print('')
print(new_list2)
print('')
print(len(new_list2))

