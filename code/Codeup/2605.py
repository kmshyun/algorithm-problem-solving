import sys
sys.setrecursionlimit(10**6)
g = [list(map(int, input().split())) for _ in range(7)]

visited = [[False] * 7 for _ in range(7)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, target):
    visited[r][c] = True
    count = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < 7 and 0 <= nc < 7:
            if not visited[nr][nc] and g[nr][nc] == target:
                count += dfs(nr, nc, target)

    return count

s = 0

for i in range(7):
    for j in range(7):
        if not visited[i][j]:
            num = g[i][j]
            size = dfs(i, j, num)
            if size >= 3:
                s += 1
print(s)