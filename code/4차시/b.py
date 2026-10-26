n, k = map(int, input().split())
l = list(map(int, input().split()))
s = [0] * (n+1)
s[1] = l[0]

for i in range(1, n+1):
    s[i] = s[i-1] + l[i-1]

r = s[k]
d = 0
for j in range(n-k+1):
    c = s[j+k] - s[j]
    if c > r:
        r = c
        d = j
        
print(d+1, r)