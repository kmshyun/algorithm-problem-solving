n, m = map(int, input().split())
c = sorted(input().split())
g = {i:[] for i in c}
visited = {i:False for i in c}

for i in range(m):
    a, b = input().split()
    g[a].append(b)
    g[b].append(a)

s = input()
d = [s]
o = []

def dfs(s):
    g[s].sort()
    visited[s] = True
    for i in g[s]:
        if not visited[i]:
            d.append(i)
            visited[i] = True
            dfs(i)

    o.append(s)

dfs(s)
print("ENTER: ", end='')
print(*d)
print("EXIT: ", end='')
print(*o)