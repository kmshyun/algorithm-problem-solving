n, m = map(int ,input().split())
l = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

for i in range(1,n+1):
    print(f"{i}:", *sorted(l[i]))