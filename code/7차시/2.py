n, m, s= map(int ,input().split())
l = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

if l[s]:
    print(*sorted(l[s]))
else:
    print("NONE")