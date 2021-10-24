file = open('names.txt', 'r')
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V','W', 'X', 'Y', 'Z']
summ = 0 
lines = (file for file in file.readlines())
y = []
tst = [k.split(',') for k in lines]
#print(len(tst[0]))
#print(tst[0].index('"COLIN"'))
#print(sorted(tst[0])[938 - 1])
#print(sorted(tst[0]).index('"COLIN"') + 1)
final = 0
for i in sorted(tst[0]):
    o =  0
    #print(n)
    for a in i:
        if a == '"' or a == ',':
            continue
        o += int(alphabet.index(a) + 1)
    #print(n)
    #print(o)
    #print(o *(tst[0].index(n)+1))
    
    final += o *(sorted(tst[0]).index(i)+1)
    #break

print(final)
