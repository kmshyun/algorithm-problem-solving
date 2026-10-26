line = input()
stack = []
cnt = 0

for i in range(len(line)):
    if line[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if line[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)