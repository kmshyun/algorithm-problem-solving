from collections import deque
n = int(input())
g = [[0 for _ in range(n)] for _ in range(n)]

dr = [2, 2, -2, -2, -1, -1, 1, 1]
dc = [1, -1, 1, -1, 2, -2, 2, -2]

sr, sc = map(int, input().split())
sr, sc = sr - 1, sc - 1

tr, tc = map(int, input().split())
tr, tc = tr - 1, tc - 1

visited  = [[False] * (n) for _ in range(n)]
visited[sr][sc] = True
q = deque([(sr, sc)])


while q:
    r, c = q.popleft()
    if r == tr and c == tc:
        break
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc]:
                g[nr][nc] = g[r][c] + 1
                visited[nr][nc] = True
                q.append((nr, nc))

print(g[tr][tc])