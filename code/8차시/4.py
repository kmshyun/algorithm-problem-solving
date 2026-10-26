from collections import deque
import sys
input = sys.stdin.readline

a, b, k, s = map(int, input().split())
g = [[] for _ in range(a + 1)]

for _ in range(b):
    v, l = map(int, input().split())
    g[v].append(l)
    g[l].append(v)

dist = [-1] * (a + 1)
dist[s] = 0
q = deque([s])

while q:
    v = q.popleft()
    
    if dist[v] == k:
        continue

    for w in g[v]:
        if dist[w] == -1:
            dist[w] = dist[v] + 1
            q.append(w)

r = [i for i in range(1, a + 1) if dist[i] == k]

if r:
    print(*r)
else:
    print(-1)