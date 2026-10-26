import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
g = [[] for _ in range(v + 1)]
rg = [[] for _ in range(v + 1)]

for _ in range(e):
    u, v_node, w = map(int, input().split())
    g[u].append((v_node, w))
    rg[v_node].append((u, w))

def dj(st, gr):
    dist = [INF] * (v + 1)
    dist[st] = 0

    pq = []
    heapq.heappush(pq, (0, st))

    while pq:
        d, cur = heapq.heappop(pq)

        if d > dist[cur]:
            continue

        for nxt, w in gr[cur]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(pq, (d + w, nxt))

    return dist

go = dj(1, g)[1:]
print(*go)
