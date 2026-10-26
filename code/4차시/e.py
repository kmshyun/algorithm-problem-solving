n, k = map(int, input().split())
l = list(map(int, input().split()))

cur = sum(l[:k])
best = cur
m = 0
for j in range(1, n - k + 1):
    cur = cur - l[j-1] + l[j+k-1]
    if cur < best:
        best = cur
        m = j

print(m + 1, best)
