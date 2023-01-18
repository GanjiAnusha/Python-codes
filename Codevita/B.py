#snake and laders
z = 10
board = []
for k in range(z):
    if k % 2 == 1: board = input().split() + board
    else: board = input().split()[::-1] + board
board = ['0'] + board
memo = ['0'] * 101
mp = {'Start': 1, 'End': 100}
for k, v in enumerate(board):
    if (v[0] == 'S' or v[0] == 'L') and v[1] == '(':
        if v[2].isdigit():
            memo[k] = int(v[2:-1])
        else: memo[k] = mp[v[2:-1]]
    else:
        memo[k] = mp.get(v[2:-1], k)
dice = list(map(int, input().split()))
curr = 0
s, l = 0, 0
for v in dice:
    if curr + v < 101: curr += v
    while memo[curr] != curr: 
        if curr > memo[curr]: s += 1
        else: l += 1
        curr = memo[curr]
if curr == 100:
    print(f'Possible {s} {l}')
else: 
    print(f'Not possible {s} {l} {"Start" if curr == 1 else curr}')