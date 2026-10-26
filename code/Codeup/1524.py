import sys

g = []
for _ in range(9):
    g.append(input().split())

r, c = map(int, input().split())
r -= 1
c -= 1

if g[r][c] == '1':
    print(-1)
    sys.exit(0)

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

m = 0

for i in range(8):
    nr = r + dr[i]
    nc = c + dc[i]

    if 0 <= nr < 9 and 0 <= nc < 9:
        if g[nr][nc] == '1':
            m += 1

print(m)