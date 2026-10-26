s = list(input())
r = []
c = 0

while s:
    if c > 0 and c % 3 == 0:
        r.append(',')
    r.append(s.pop())
    c += 1

print(''.join(r[::-1]))