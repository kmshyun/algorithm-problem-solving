from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
g = [input() for _ in range(a)]

sr = 0
sc = 0
tr = a-1
tc = b-1

d = [[-1] * b for i in range(a)]
d[sr][sc] = 0
q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    if r == tr and c == tc:
        break

    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= nr < a and 0 <= nc < b and g[nr][nc] == '1' and d[nr][nc] == -1:
            q.append((nr, nc))
            d[nr][nc] = d[r][c] + 1

print(d[tr][tc] + 1)
