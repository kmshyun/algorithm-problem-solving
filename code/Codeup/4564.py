n = int(input())
l = [0]
m = [0] * (n+1)
for i in range(n):
    l.append(int(input()))

m[1] = l[1]
if n >= 2: 
    m[2] = l[1] + l[2]
if n >= 3:
    m[3] = max(l[1] + l[3], l[2] + l[3])

if n >= 3:
    for i in range(3, n+1):
        m[i] = max(m[i-2] + l[i], m[i-3] + l[i-1] + l[i])

print(m[n])


'''
an = 현재까지 값
sn = 현재 계단의 값

a(n) = max(a(n-2) + s(n),  a(n-3) + s(n-1) + s(n))


'''