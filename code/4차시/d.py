n, k, r = map(int, input().split())
l = list(map(int, input().split()))
s = []
for i in l:
    if i >= r:
        s.append(1)
    else:
        s.append(0)

ss = [0] * (n+1)
for i in range(1, n+1):
    ss[i] = ss[i-1] + s[i-1]

for j in range(k):
    a, b = map(int, input().split())
    print(ss[b] - ss[a-1])

