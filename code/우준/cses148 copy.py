import sys
input = sys.stdin.readline
INF = float('inf')

v, e, q = map(int, input().split())
d = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    d[i][i] = 0

for _ in range(e):
    a, b, w = map(int, input().split())
    if w < d[a][b]:
        d[a][b] = d[b][a] = w

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]

ans = []
for _ in range(q):
    a, b = map(int, input().split())
    res = d[a][b]
    ans.append(res if res != INF else -1)

print('\n'.join(map(str, ans)))