n = int(input())
l = []
def b(s):
    if len(l) == s:
        print(*l)
        return
    for i in ['0', '1']:
        l.append(i)
        b(s)
        l.pop()

b(n)