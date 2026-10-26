a, b, s = map(int, input().split())
g = [[] for _ in range(a + 1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

v = [0] * (a + 1)
l = [s]

def dfs(s):
    v[s] = 1
    for i in g[s]:
        if not v[i]:
            l.append(i)
            dfs(i)
            
dfs(s)
print(sum(v))
print(*sorted(l))