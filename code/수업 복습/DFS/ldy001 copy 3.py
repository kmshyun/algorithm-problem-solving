from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nodes = sorted(input().split())

g = {i: [] for i in nodes}
visited = {i: False for i in nodes}

for _ in range(m):
    a, b = input().split()
    g[a].append(b)
    g[b].append(a)

for i in nodes:
    g[i].sort()

s, t = input().split()

dist = {i: -1 for i in nodes}
p = {i: None for i in nodes}
q = deque([s])

visited[s] = True
dist[s] = 0

while q:
    cur = q.popleft()
    if cur == t:
        break
    for nxt in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dist[nxt] = dist[cur] + 1
            p[nxt] = cur
            q.append(nxt)

if not visited[t]:
    print(-1)
    print("NONE")
else:
    print(dist[t])
    path = []
    curr = t
    while curr is not None:
        path.append(curr)
        curr = p[curr]
    print(*path[::-1])