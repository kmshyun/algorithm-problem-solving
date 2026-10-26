import sys
sys.setrecursionlimit(100000)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, h, visited):
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc] and g[nr][nc] > h:
                dfs(nr, nc, h, visited)

mh = max(max(row) for row in g)

mc = 1
for h in range(int(mh)):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and g[r][c] > h:
                dfs(r, c, h, visited)
                cnt += 1
    mc = max(mc, cnt)

print(mc)