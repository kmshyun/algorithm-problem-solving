n = int(input())
s = list(map(int, input().split()))


cur = sum(s[:30])
best = cur
m = 0
for j in range(1, n - 30 + 1):
    cur = cur - s[j-1] + s[j+30-1]
    if cur > best:
        best = cur
        m = j

print(m + 1, best)