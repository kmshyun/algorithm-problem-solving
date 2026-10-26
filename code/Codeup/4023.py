import sys

g = []
for _ in range(19):
    g.append(input().split())

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]


def dfs(x, y, d, c):
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < 19 and 0 <= ny < 19 and g[nx][ny] == c:
            return 1 + dfs(nx, ny, d, c)
        
    return 1

for i in range(19):
    for j in range(19):
        if g[i][j] != '0':
            color = g[i][j]
            for d in range(4):
                cnt = dfs(i, j, d, color)

                if cnt == 5:
                    px = i - dx[d]
                    py = j - dy[d]

                    if 0 <= px < 19 and 0 <= py < 19 and g[px][py] == color:
                        continue
                    print(color)
                    print(i+1, j+1)
                    sys.exit(0)


print(0)