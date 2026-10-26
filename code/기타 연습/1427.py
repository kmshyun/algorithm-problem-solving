n = list(input())
l = []
for i in n:
    l.append(int(i))
l.sort(reverse=True)
for i in l:
    print(i, end='')
