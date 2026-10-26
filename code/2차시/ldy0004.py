n, k = map(int, input().split())
a = set(input().split())
b = input().split()
l = []
for i in b:
    if i not in a:
        l.append(i)

print(' '.join(l) if l else "NONE")