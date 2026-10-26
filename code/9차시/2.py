import sys
import heapq

input = sys.stdin.readline
q = int(input())
heap = []
output = []

for _ in range(q):
    cmd = input().split()

    if cmd[0] == '1':
        id = int(cmd[1])
        p = int(cmd[2])
        heapq.heappush(heap, (p, id))
    else:
        if heap:
            p, id = heapq.heappop(heap)
            output.append(str(id))
        else:
            output.append("EMPTY")

print("\n".join(output))