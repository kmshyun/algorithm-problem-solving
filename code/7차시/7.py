a, b = map(int, input().split())
g = [[] for _ in range(a + 1)]
r = [i for i in range(1, a+1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

v = [0] * (a + 1)
n = 0

def dfs(s):
    v[s] = True
    for i in g[s]:
        if not v[i]:
            dfs(i)


for i in range(1, a+1):
    if not v[i]:
        dfs(i)
        n += 1

print(n)