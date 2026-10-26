n, k = map(int ,input().split())
a = set(input().split())
b = list(input().split())
for i in b:
    if i in a:
        print("YES")
    else:
        print("NO")