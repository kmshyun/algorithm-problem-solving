n = int(input())
k = input().split()
m = {}
for i in k:
    m[i] = m.get(i, 0) + 1

s = int(input())
l = list(input().split())
for i in l:
    if i not in m.keys():
        print(0)
    else:
        print(m[i])