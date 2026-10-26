from collections import deque
n = int(input())
r, c = map(int, input().split())
g = [[0 for _ in range(n)] for _ in range(n)]

r -= 1
c -= 1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

visited  = [[False] * (n) for _ in range(n)]
visited[r][c] = True
q = deque([(r, c)])
d = [[0 for _ in range(n)] for _ in range(n)]
d[r][c] = 1


while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc] and abs(g[r][c] - g[nr][nc]) <= 1:
                d[nr][nc] = d[r][c] + 1
                visited[nr][nc] = True
                q.append((nr, nc))

for i in d:
    print(*i)