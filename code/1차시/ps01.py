n = int(input())
l = list(map(int, input().split()))
s = 0
w = 0

for i in l:
    s += i
    if i >= 1000:
        w += 1

print(round(s/n, 1))
print(w)