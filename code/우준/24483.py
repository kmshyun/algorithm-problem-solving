n, m, p = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [False] * (n+1)
pp = [p]
ppp = [-1] * (n+1)
ppp[p] = 0
k = 1
def dfs(s):
    global k
    g[s].sort(reverse = True)
    v[s] = True
    for i in g[s]:
        if not v[i]:
            ppp[i] = ppp[s] + 1
            pp.append(i)
            dfs(i)



dfs(p)
s = 0
for i in range(1, n+1):
    if i in pp:
        s += (pp.index(i) + 1) * (ppp[i])
print(s)