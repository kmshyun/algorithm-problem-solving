n, k = map(int, input().split())
l = list(map(int, input().split()))
s = [0] * (n+1)
s[1] = l[0]
for i in range(1, n+1):
    s[i] = s[i-1] + l[i-1]


for j in range(k):
    a, b = map(int, input().split())
    print(s[b] - s[a-1])