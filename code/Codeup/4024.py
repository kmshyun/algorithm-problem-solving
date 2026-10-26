import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

w, h = map(int, input().split())
g = []
for _ in range(h):
    g.append(input().split())

visited = [[False] * w for _ in range(h)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w:
            if not visited[nx][ny] and g[nx][ny] == 'L':
                dfs(nx, ny)

count = 0
for i in range(h):
    for j in range(w):
        if not visited[i][j] and g[i][j] == 'L':
            dfs(i, j)
            count += 1

print(count)