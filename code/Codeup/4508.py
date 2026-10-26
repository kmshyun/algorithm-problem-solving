from collections import deque
n = int(input())
k = int(input())
g = [[] for i in range(n+1)]
r = []
for _ in range(k):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)
def bfs(s):
    d = [-1] * (n + 1)
    d[s] = 0
    q = deque([s])
    md = 0
    while q:
        c = q.popleft()
        for i in g[c]:
            if d[i] == -1:
                d[i] = d[c] + 1
                if d[i] > md:
                    md = d[i]
                q.append(i)
    return md

for i in range(1, n + 1):
    if not visited[i]:
        cp = [i]
        visited[i] = True
        q = deque([i])
        while q:
            curr = q.popleft()
            for nxt in g[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cp.append(nxt)
                    q.append(nxt)
        
        br = -1
        mmd = float('inf')
        for m in cp:
            mdist = bfs(m)
            if mdist < mmd:
                mmd = mdist
                br = m
                
        r.append(br)

print(len(r))
for rep in sorted(r):
    print(rep)