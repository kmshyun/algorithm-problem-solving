import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(input().split())

INF = float('inf')
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0

dr = [-1,1,0,0]
dc = [0,0,-1,1]

pq = []
heapq.heappush(pq, (0,(0,0)))

while pq:
    time, cor = heapq.heappop(pq)
    r, c = cor
    if time > dist[r][c]:
        continue

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if time + int(g[nr][nc]) < dist[nr][nc]:
                dist[nr][nc] = time + int(g[nr][nc])
                heapq.heappush(pq, (time + int(g[nr][nc]), (nr, nc)))

print(dist[n-1][m-1])