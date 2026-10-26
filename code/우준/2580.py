g = [list(map(int, input().split())) for _ in range(9)]
e = []

def find_empty():
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                return (i, j)

def check_empty(): # 빈칸 있나 확인
    for i in range(9):
        for j in range(9):
            if g[i][j] == 0:
                return True
    return False


# 아래 Check 코드는 모두 k가 '없으면' True를 반환

def check_mt(n, k): # 뭉탱이 안에 k가 있는지 확인 좌상단부터 1 2 3  .. 9
    row = (n-1) // 3
    col = (n-1) % 3
    for i in range(row * 3, row *3 + 3):
        for j in range(col * 3, col * 3 + 3):
            if g[i][j] == k:
                return False
    return True

def check_row(row, k):
    if k in g[row]:
        return False
    return True

def check_col(col, k):
    for i in range(9):
        if g[i][col] == k:
            return False
    return True

def b():
    if not check_empty():
        return True
    row, col = find_empty()
    num = (row // 3) * 3 + (col // 3) + 1
    for i in range(1, 10):
        if not (check_row(row, i) and check_col(col, i) and check_mt(num, i)):
            continue
        g[row][col] = i
        if b():
            return True
        g[row][col] = 0

    g[row][col] = 0

b()
for i in g:
    print(*i)

'''
row, col을 3으로 나눴을때 몫
row : 
0 0 0 1 1 1 2 2 2

col : 
0
0
0
1
1
1
2
2
2

row + col
0 
'''


