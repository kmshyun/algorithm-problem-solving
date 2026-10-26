from collections import deque
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

visited  = [[False] * (m) for _ in range(n)]
visited[0][0] = True
q = deque([(0, 0)])
d = [[0 for _ in range(m)] for _ in range(m)]
d[0][0] = 1


while q:
    r, c = q.popleft()
    if r == n-1 and c == m-1:
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc] and abs(g[r][c] - g[nr][nc]) <= 1:
                d[nr][nc] = d[r][c] + 1
                visited[nr][nc] = True
                q.append((nr, nc))

print(d[n-1][m-1])