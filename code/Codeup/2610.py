import sys
input = sys.stdin.readline
g = []
for _ in range(10):
    g.append(list(input().strip()))

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * 10 for _ in range(10)]

def check_color(x, y):
    cnt = 4
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            if g[ny][nx] == '*':
                cnt -= 1
        elif nx >= 10 or ny >= 10 or nx < 0 or ny < 0:
            cnt -= 1
    return cnt

def dfs(x, y):
    visited[y][x] = True
    g[y][x] = '*'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            if not visited[ny][nx] and g[ny][nx] == '_':
                dfs(nx, ny)

if 0 <= m < 10 and 0 <= n < 10 and g[m][n] == '_':
    dfs(n, m)

for row in g:
    print(''.join(row))