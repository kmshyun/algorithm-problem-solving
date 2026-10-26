n = int(input())
s = []
for i in range(n):
    c = input()
    if 'push' in c:
        k = c.split(' ')[1]
        s.append(k)
    elif c == 'top()':
        print(-1 if not s else s[-1])
    elif c == 'pop()':
        if s:
            s.pop()
    elif c == 'empty()':
        print('true' if not s else 'false')
    else:
        print(len(s))