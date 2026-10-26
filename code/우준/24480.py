n, m, p = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [False] * (n+1)
pp = [p]
k = 1
def dfs(s):
    global k
    g[s].sort(reverse = True)
    v[s] = True
    for i in g[s]:
        if not v[i]:
            pp.append(i)
            dfs(i)



dfs(p)
for i in range(1, n+1):
    if i not in pp:
        print(0)
    else:
        print(pp.index(i)+1)