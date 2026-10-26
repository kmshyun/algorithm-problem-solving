from collections import deque

n, m = map(int, input().split())
g = [input().split() for _ in range(n)]

q = deque([(0,0)])
d = [[0 for _ in range(m)] for _ in range(n)]
d[0][0] = 1

dr = [0,0,-1,1]
dc = [-1,1,0,0]

while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if not d[nr][nc] and abs(int(g[nr][nc]) - int(g[r][c])) <= 1:
                d[nr][nc] = d[r][c] + 1
                q.append((nr, nc))

print(d[n-1][m-1])