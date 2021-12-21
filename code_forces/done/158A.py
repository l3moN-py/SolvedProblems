n,k = map(int, input().split())
scores = list(map(int, input().split()))
place = scores[k-1]
print(len(list(filter(lambda x:x>=place and x>0, scores))))