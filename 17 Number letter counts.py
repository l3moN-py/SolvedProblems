dc1 = {0: '',1: 'One',2: 'Two',3: 'Three',4: 'Four',5: 'Five',6: 'Six',7: 'Seven',8: 'Eight',9: 'Nine',10: 'Ten',11: 'Eleven',12: 'Twelve',13: 'Thirteen',14: 'Fourteen',15: 'Fifteen',16: 'Sixteen',17: 'Seventeen',18: 'Eighteen',19: 'Nineteen'}
dc2 = {0: '', 20 : 'Twenty', 30 : 'Thirty', 40 :'Forty', 50 : 'Fifty', 60 : 'Sixty', 70 :'Seventy',80 : 'Eighty', 90 : 'Ninety'}
y = []
def number(num):
    if 1 <= num < 20:
        return dc1[num]
    elif 20 <= num < 100:
        if num in dc2:
            return dc2.get(num)
        return dc2[int(str(num)[0]+'0')] + dc1[int(str(num)[1])]
    elif 100 <= num:
        if str(num)[1] == '0' and str(num)[2] == '0':
            return dc1[int(str(num)[0])] + 'Hundred'
        return dc1[int(str(num)[0])] + 'Hundred' + 'And' + number(int(str(num)[1:3]))

for a in range(1,1000):
    y.append(number(a))
y.append('OneThousand')
#print(y)
y = ''.join(y)
print(len(y))
