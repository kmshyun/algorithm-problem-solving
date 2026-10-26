from collections import deque
import sys
input = sys.stdin.readline

a, b, s= map(int, input().split())
g = [[] for _ in range(a + 1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

r = []
dist = [-1] * (a + 1)
dist[s] = 0
q = deque([s])

while q:
    v = q.popleft()

    for w in g[v]:
        if dist[w] == -1:
            dist[w] = dist[v] + 1
            q.append(w)

print(*dist[1:])