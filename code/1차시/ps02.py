n = int(input())
l = list(map(int, input().split()))
m = l[0]
id = 0
h = 13
min = 00

for i in l:
    if m <= i:
        m = i
        id = l.index(i)

print(m)
h = 13 + (5*id)//60
min = str((5 * id)%60)
if len(min) <= 1:
    min = '0'+ min
print(f"{h}:{min}")