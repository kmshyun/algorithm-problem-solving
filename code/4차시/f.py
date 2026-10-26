n, k, r = map(int, input().split())
l = list(map(int, input().split()))
s = []
for i in l:
    if i >= r:
        s.append(1)
    else:
        s.append(0)


cur = sum(s[:k])
best = cur
m = 0
for j in range(1, n - k + 1):
    cur = cur - s[j-1] + s[j+k-1]
    if cur > best:
        best = cur
        m = j

print(m + 1, best)