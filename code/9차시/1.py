import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

for i in range(1, n + 1):
    adj[i].sort(key=lambda x: x[0])
    output = [i, len(adj[i])]
    
    for neighbor, time in adj[i]:
        output.append(neighbor)
        output.append(time)
        
    print(*(output))