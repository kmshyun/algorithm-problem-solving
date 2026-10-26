import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    line = input().strip()
    if not line:
        return
    n = int(line)

    ULL_MAX = (1 << 64) - 1

    q = deque([1])

    while q:
        cur = q.popleft()

        if cur > ULL_MAX:
            break

        if cur % n == 0:
            print(cur)
            return

        nxt0 = cur * 10
        nxt1 = cur * 10 + 1

        if nxt0 <= ULL_MAX:
            q.append(nxt0)
        if nxt1 <= ULL_MAX:
            q.append(nxt1)

    print(0)

solve()