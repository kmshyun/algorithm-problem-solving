n, m = map(int, input().split())
c = input().split()
g = {i:[] for i in c}
for i in range(m):
    a, b = input().split()
    g[a].append(b)
    g[b].append(a)

for i in sorted(g):
    print(f"{i}: ", end='')
    print(*sorted(g[i]))