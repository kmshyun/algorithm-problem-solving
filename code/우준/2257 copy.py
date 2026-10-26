s = input()
e = {"H" : 1, "C" : 12, "O" : 16}
stack = []
q = ''

def number():
    global q
    if q:
        prev = stack.pop()
        stack.append(prev * int(q))
        q = ''

for i in s:
    if i.isdigit():
        q += i
    else:
        number()
        if i in e:
            stack.append(e[i])
        elif i == '(':
            stack.append('(')
        elif i == ')':
            k = 0
            while stack[-1] != '(':
                k += stack.pop()
            stack.pop()
            stack.append(k)
number()
print(sum(stack))