x= [1,1]

while len(str(x[::-1][0])) < 1000:
    x.append(x[::-1][0]+x[::-1][1])

#print(x)
print(len(x))
