from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
g = [[] for _ in range(a + 1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)
    
s, t = map(int, input().split())
dist = [-1] * (a+1)
dist[s] = 0
q = deque([s])

while q:
    v = q.popleft()
    if v == t:
        break

    for w in g[v]:
        if dist[w] != -1:
            continue
        q.append(w)
        dist[w] = dist[v] + 1


print(dist[t])