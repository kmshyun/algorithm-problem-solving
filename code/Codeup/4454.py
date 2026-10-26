from collections import deque

n= int(input())
a, b = map(int, input().split())
k = int(input())

g = [[] for _ in range(n+1)]
for i in range(k):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

visited = [False] * (n+1)
distance = [0] * (n+1)
q = deque([a])

def bfs(a, b):
    visited[a] = True
    while q:
        c = q.popleft()
        if c == b:
            return distance[b]
        for i in g[c]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[c] + 1
                q.append(i)

    return -1

print(bfs(a, b))