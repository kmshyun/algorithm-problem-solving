n = int(input())
l = []
    # for i in range(2**n):
    #     k = '0' * (n - len(bin(i)[2:])) + bin(i)[2:]
    #     print(' '.join(list(k)))


def b():
    # base case
    if len(l) == n:
        print(*l)
        return

    # recursive case

    for i in [0, 1]:
        # 후보 선택
        l.append(i)

        # 탐색
        b()

        # 마지막꺼 pop
        l.pop()

b()


    