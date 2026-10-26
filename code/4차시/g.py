n, k = map(int, input().split())
l = input().split()

f = {}
for x in l[:k]:
    f[x] = f.get(x, 0) + 1

best = len(f)
m = 0

for i in range(1, n - k + 1):
    inc = l[i + k - 1]
    og = l[i - 1]
    f[inc] = f.get(inc, 0) + 1
    f[og] -= 1
    if f[og] == 0:
        del f[og]

    if len(f) > best:
        best = len(f)
        m = i
print(m + 1, best)