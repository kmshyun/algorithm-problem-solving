goal = []
n = int(input())
for i in range(n):
    goal.append(int(input()))

cur = 1
stack = []
ans = []

for i in goal:
    while cur <= i:
        stack.append(cur)
        ans.append('+')
        cur += 1
    if stack and stack[-1] == i:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        exit()

for i in ans:
    print(i)