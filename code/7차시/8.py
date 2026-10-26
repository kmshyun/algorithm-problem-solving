a, b, s, t = map(int, input().split())
g = [[] for _ in range(a + 1)]
r = [i for i in range(1, a+1)]

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

for i in g:
    i.sort()

vi = [0] * (a + 1)
n = 0
l = []

def dfs(c,ct):
    global t
    l.append(c)
    if c == t:
        print(ct)
        print(*l)
        return True
    vi[c]=True

    for v in g[c]:
        if vi[v]:
            continue
        if dfs(v,ct+1):
            return True
        l.pop()
    
    return False

if not dfs(s,1):
    print('NO PATH')