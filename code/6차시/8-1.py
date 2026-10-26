n, k = map(int, input().split())
l = []
h = []
for i in range(k):
    a, b = map(int, input().split())
    h.append([a,b])

def b():
    if len(l) == n:
        return 1

    c = 0
    for r in range(n):
        #제약조건 검사 --> 후보 제외
        if not con(r):
            continue

        #후보 선택
        l.append(r)

        #계속 탐색
        c += b()
        
        #이전 상태로 되돌리기
        l.pop()

    return c

def con(r):
    if r in l:
        return False
    for i in h:
        if r == i[0] - 1 and len(l) == i[1] - 1:
            return False
    for i in l:
        if abs(l.index(i) - (len(l))) == abs(i - r):
            return False
    return True

# con 함수는 Bool 값을 return
print(b())