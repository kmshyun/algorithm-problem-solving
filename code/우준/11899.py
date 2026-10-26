l = input()
s = []
for i in l:
    if i == '(':
        s.append(i)
    else:
        if s and s[-1] == '(':
            s.pop()
        else:
            s.append(i)
 
print(len(s))