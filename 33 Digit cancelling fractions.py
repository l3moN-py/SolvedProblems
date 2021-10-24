res = []
def multiplyList(myList) :

    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

for a in range(10,100):
    for b in range(a + 1,100):
        s = str(a) + str(b)

        for i in [_ for _ in range(1,10)]:
            i = str(i)
            if s.count(i) >= 2:
                a2 = str(a).replace(i, '')
                b2 = str(b).replace(i, '')
                if a2 != '' and b2 != '' and int(b2) != 0 and a/b == int(a2)/int(b2):
                    res.append([int(a2), int(b2)])
                break
numerator = multiplyList([a[0] for a in res])
denominator = multiplyList([a[1] for a in res])
#print(numerator)
#print(denominator)
print('Answer:', denominator//numerator)
