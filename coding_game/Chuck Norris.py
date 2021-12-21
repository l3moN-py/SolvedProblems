l = list('10000111000011')
for i in range(len(l)-1):
    if l[i] != l[i+1]:
        if l[i]=='1':
            l[i] = '1x'
        else:
            l[i] = '0x'
x=''.join(l).split('x')
print(' '.join([' '.join(['0', '0'*a.count('1')]) if a[0]=='1' else ' '.join(['00', '0'*a.count('0')]) for a in x]))
