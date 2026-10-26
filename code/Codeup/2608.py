n = int(input())
l = []
def b():
    if len(l) == n:
        print(''.join(l))
        return

    for i in ['O', 'X']:
        l.append(i)
        b()
        l.pop()
b()