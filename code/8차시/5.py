from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
g = [[] for _ in range(a + 1)]

for _ in range(b):
    v, l = map(int, input().split())
    g[v].append(l)
    g[l].append(v)

s, t = map(int ,input().split())

dist = [-1] * (a + 1)
dist[s] = 0
q = deque([s])
p = [-1] * (a + 1)

while q:
    v = q.popleft()
    if v == t:
        break

    for w in g[v]:
        if dist[w] == -1:
            dist[w] = dist[v] + 1
            q.append(w)
            p[w] = v

print(dist[t])
path =[]
c = t
while c != -1:
    path.append(c)
    c = p[c]

print(*path[::-1])