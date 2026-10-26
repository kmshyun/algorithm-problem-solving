l = list(input())
s = []
m = True

for i in l:
    if i == '(':
        s.append(i)
    else:
        if not s:
            m = False
            break
        s.pop()

if m and not s:
    print("YES")
else:
    print("NO")