from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]

q = deque()
for i in range(m):
    for j in range(n):
        if g[i][j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if g[nx][ny] == 0:
                g[nx][ny] = g[x][y] + 1
                q.append((nx, ny))

ans = 0
for row in g:
    for val in row:
        if val == 0:
            print(-1)
            exit(0)

    ans = max(ans, max(row))

print(ans-1)