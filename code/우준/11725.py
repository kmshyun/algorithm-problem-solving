n = int(input())
g = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [False] * (n+1)
p = [0] * (n+1)
def dfs(s):
    v[s] = True
    for i in g[s]:
        if not v[i]:
            p[i] = s
            dfs(i)



dfs(1)
for i in p:
    if i != 0:
        print(i)