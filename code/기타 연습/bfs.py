from collections import deque

n = int(input())
k = int(input())
g = [[] for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n+1)
def bfs(s):
    q = deque([s])
    visited[s] = True

    while q:
        c = q.popleft()
        for i in g[c]:
            if not visited[i]:
                print(i)
                visited[i] = True
                q.append(i) 


bfs(1)