n, m, p = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [False] * (n+1)
pp = [-1] * (n+1)
pp[p] = 0
def dfs(s):
    g[s].sort(reverse = True)
    v[s] = True
    for i in g[s]:
        if not v[i]:
            pp[i] = pp[s] + 1
            dfs(i)



dfs(p)
for i in range(1, n+1):
    print(pp[i])