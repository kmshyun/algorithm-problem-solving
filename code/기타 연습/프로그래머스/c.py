a, b = map(int, input().split())
l = list(map(int, input().split()))
k = 0
for i in range(a):
    for j in range(a):
        if i > j and l[i] + l[j] == b:
            k += 1
print(k)