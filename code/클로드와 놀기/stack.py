n = int(input())
goal = list(map(int, input().split()))
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

print(' '.join(ans))