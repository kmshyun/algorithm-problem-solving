import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())
s, t = map(int, input().split())
g = [[] for _ in range(v + 1)]

times = 0

for _ in range(e):
    u, v_node, w = map(int, input().split())
    g[u].append((v_node, w))

for k in range(1, v+1):
    dist = [INF] * (v + 1)
    dist[s] = 0

    pq = []
    heapq.heappush(pq, (0, s))

    while pq:
        d, cur = heapq.heappop(pq)
        
        if d > dist[cur]:
            continue

        for nxt, w in g[cur]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(pq, (d + w, nxt))

    distance = dist[k]


    dist = [INF] * (v + 1)
    dist[k] = 0

    pq = []
    heapq.heappush(pq, (0, k))

    while pq:
        d, cur = heapq.heappop(pq)
        
        if d > dist[cur]:
            continue

        for nxt, w in g[cur]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(pq, (d + w, nxt))

    distance += dist[s]
    if distance <= t:
        times += 1

print(times - 1) # Start to Start를 미리 안빼서 이렇게 했어유
