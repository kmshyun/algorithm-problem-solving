from collections import deque
n, k = map(int, input().split())
l = input().split()
g = {i: [] for i in l}

for i in range(k):
    a, b = input().split()
    g[a].append(b)
    g[b].append(a)

s = input()

dist = {i:0 for i in l}
dist[s] = 0
visited = {i:False for i in l}
q = deque([s])

while q:
    cur = q.popleft()
    visited[cur] = True
    for i in g[cur]:
        if not visited[i]:
            dist[i] = dist[cur] + 1
            visited[i] = True
            q.append(i)

for i in sorted(dist):
    if visited[i]:
        print(f"{i}: {dist[i]}")
    else:
        print(f"{i}: -1")