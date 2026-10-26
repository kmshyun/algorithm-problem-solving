l = input()
s = []
p = {')': '(', ']': '[', '}': '{'}
v = True

for c in l:
    if c in "({[":
        s.append(c)
    elif c in ")}]":
        if not s or s[-1] != p[c]:
            v = False
            break
        s.pop()

if v and not s:
    print("YES")
else:
    print("NO")