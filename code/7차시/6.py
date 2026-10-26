a, b, s = map(int, input().split())
g = [[] for _ in range(a + 1)]
r = [i for i in range(1, a+1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

v = [0] * (a + 1)
l = [s]

def dfs(s):
    v[s] = True
    for i in g[s]:
        if not v[i]:
            l.append(i)
            dfs(i)
            
dfs(s)
l = [i for i in r if i not in l]
if l:
    print(*l)
else:
    print("ALL REACHABLE")