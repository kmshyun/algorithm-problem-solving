from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
g = [[] for _ in range(a + 1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

r = []
s, k = map(int, input().split())
l = list(map(int, input().split()))

for i in l:
    q = deque([s])
    dist = [-1] * (a+1)
    dist[s] = 0
    while q:
        v = q.popleft()
        if v == i:
            break

        for w in g[v]:
            if dist[w] != -1:
                continue
            q.append(w)
            dist[w] = dist[v] + 1

    r.append(dist[i])

if r == [-1] * len(r):
    print(-1)
else:
    x = [i for i in r if i >= 0]
    print(min(x))