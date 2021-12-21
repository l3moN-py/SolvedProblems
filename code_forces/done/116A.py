stops = int(input())
max_ppl = 0
in_ppl = 0

for stop in range(stops):
    Out, In = map(int, input().split())
    in_ppl -= Out
    in_ppl += In
    if in_ppl > max_ppl:
        max_ppl = in_ppl

print(max_ppl)