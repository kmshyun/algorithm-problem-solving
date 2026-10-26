from collections import deque
import sys
input = sys.stdin.readline

a = int(input())
l = input().split()
q = deque()

for i in l:
    q.append(i)
    
for i in range(a):
    print(q.popleft())