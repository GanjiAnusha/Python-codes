n = int(input())
m = int(input())
memo = {}
for i in range(m):
    e1, e2 = map(int, input().split())
    memo[e1] = memo.get(e1, 0) + 1
    memo[e2] = memo.get(e2, 0) + 1
wt = sorted(list(map(int, input().split())))[::-1]
dl = sorted([v for v in memo.values()])[::-1]    
sum = 0
for i, j in zip(wt, dl):
    sum += i * j
print(sum,end='')