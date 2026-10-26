import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, target):
    visited[r][c] = True
    count = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc] and g[nr][nc] == target:
                count += dfs(nr, nc, target)

    return count

max_sizes = {}

for i in range(n):
    for j in range(m):
        if not visited[i][j] and g[i][j] >= 0:
            num = g[i][j]
            size = dfs(i, j, num)
            
            if num not in max_sizes or size > max_sizes[num]:
                max_sizes[num] = size

for num in sorted(max_sizes.keys()):
    print(num, max_sizes[num])