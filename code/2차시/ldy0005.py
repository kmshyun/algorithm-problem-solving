n = int(input())
k = input().split()
m = {}
for i in k:
    m[i] = m.get(i, 0) + 1

mx = max(m.values())
for i in k:
    if m[i] == mx:
        r = i
        break
print(i, mx)