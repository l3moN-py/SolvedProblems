word1 = input().lower()
word2 = input().lower()

for i in range(len(word1)):
    if word1[i] > word2[i]:
        print(1)
        break
    elif word1[i] < word2[i]:
        print(-1)
        break
else:
    print(0)