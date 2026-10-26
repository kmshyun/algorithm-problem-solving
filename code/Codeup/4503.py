n = int(input())
k = int(input())
g = [[] for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n+1)
l = 0

def dfs(s):
    global l
    visited[s] = True
    for i in g[s]:
        if not visited[i]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        l += 1

print(l)