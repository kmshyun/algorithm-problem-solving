import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r, c, k = map(int, input().split())
g = [[0] * c for _ in range(r)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            g[i][j] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(y, x):
    g[y][x] = 1
    cnt = 1
    for i in range(4):
        ny, nx = y + dr[i], x + dc[i]
        if 0 <= ny < r and 0 <= nx < c and g[ny][nx] == 0:
            cnt += dfs(ny, nx)
    return cnt

ans = []
for i in range(r):
    for j in range(c):
        if g[i][j] == 0:
            ans.append(dfs(i, j))

ans.sort()
print(len(ans))
print(*ans)