tokens = input().split()
stack = []

for token in tokens:
    try:
        stack.append(int(token))
    except ValueError:
        right = stack.pop()
        left = stack.pop()

        if token == '+':
            stack.append(left + right)
        elif token == '-':
            stack.append(left - right)
        elif token == '*':
            stack.append(left * right)

print(stack[0])