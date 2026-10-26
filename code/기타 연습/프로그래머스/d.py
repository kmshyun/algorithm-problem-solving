import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
cur = 0
l = 0

for r in range(n):
    cur += a[r]
    while cur > s and l <= r:
        cur -= a[l]
        l += 1
    if cur <= s and l <= r:
        ans = max(ans, r - l + 1)

print(ans)