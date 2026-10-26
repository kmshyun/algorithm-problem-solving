from collections import deque
n, k = map(int, input().split())
l = input().split()
g = {i: [] for i in l}

for i in range(k):
    a, b = input().split()
    g[a].append(b)
    g[b].append(a)

s = input()

bway = [s]
dway = [s]
visited = {i:False for i in l}
q = deque([s])

while q:
    cur = q.popleft()
    g[cur].sort()
    visited[cur] = True
    for i in g[cur]:
        if not visited[i]:
            bway.append(i)
            visited[i] = True
            q.append(i)

visited = {i:False for i in l}

def dfs(c):
    g[c].sort()
    visited[c] = True
    for i in g[c]:
        if not visited[i]:
            visited[i] = True
            dway.append(i)
            dfs(i)

dfs(s)
print("DFS: ", end = '')
print(*dway)
print("BFS: ", end = '')
print(*bway)
print("COMMON: ", end = '')
print(*sorted(bway))