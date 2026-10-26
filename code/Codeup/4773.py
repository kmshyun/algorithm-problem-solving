from collections import deque
import sys
input = sys.stdin.readline

n, m, h= map(int, input().split())
g = []
for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(m)]
    g.append(layer)

q = deque()
for z in range(h):
    for y in range(m):
        for x in range(n):
            if g[z][y][x] == 1:
                q.append((z, y, x))

dx = [0, 0, 1, -1, 0, 0]
dy = [1, 0, 0, 0, 0, -1]
dz = [0, 1, 0, 0, -1, 0]

while q:
    z, y, x = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if g[nz][ny][nx] == 0:
                g[nz][ny][nx] = g[z][y][x] + 1
                q.append((nz, ny, nx))

ans = 0
for layer in g:
    for row in layer:
        for val in row:
            if val == 0:
                print(-1)
                exit(0)
            ans = max(ans, val)

print(ans-1)