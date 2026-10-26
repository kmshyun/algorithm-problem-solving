import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(h)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, t, v):
    v[r][c] = True
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < h and 0 <= nc < w:
            if not v[nr][nc] and g[nr][nc] == t:
                dfs(nr, nc, t, v)

def solve(t):
    v = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not v[i][j] and g[i][j] == t:
                dfs(i, j, t, v)
                cnt += 1
    return cnt

print(solve(0), solve(1))