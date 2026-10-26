n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
tot = 0
ans = 0

for r in range(n):
    tot += a[r]
    
    while tot > s and l <= r:
        tot -= a[l]
        l += 1
        
    if tot <= s:
        ans = max(ans, r - l + 1)

print(ans)