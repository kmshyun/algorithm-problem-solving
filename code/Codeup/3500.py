import sys

g = []
for _ in range(9):
    g.append(input().split())

r, c = map(int, input().split())
r -= 1
c -= 1

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def cm(cr, cc):
    m = 0
    for i in range(8):
        nr = cr + dr[i]
        nc = cc + dc[i]

        if 0 <= nr < 9 and 0 <= nc < 9:
            if g[nr][nc] == '1':
                m += 1

    return m

board = [['_' for _ in range(9)] for _ in range(9)]
visited = [[False] * 9 for _ in range(9)]

def dfs(cr, cc):
    if g[cr][cc] == '1':
        board[cr][cc] = '-1'
        return
    visited[cr][cc] = True
    m = cm(cr, cc)
    board[cr][cc] = str(m)

    if m == 0:
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < 9 and 0 <= nc < 9:
                if not visited[nr][nc] and g[nr][nc] != '1':
                    dfs(nr, nc)

dfs(r, c)

for row in board:
    print(*row)