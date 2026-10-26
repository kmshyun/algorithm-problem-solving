from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

sr = 0
sc = 0

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            sr, sc = i, j

q = deque([(sr, sc)])
d = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
d[sr][sc] = 0

while q:
    r, c = q.popleft()
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if g[nr][nc] == 1 and not visited[nr][nc]:
                d[nr][nc] = d[r][c] + 1
                q.append((nr, nc))
                visited[nr][nc] = True

for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and d[i][j] == 0:
            d[i][j] = -1
     
for i in d:
    print(*i)