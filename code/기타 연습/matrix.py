s1 = input()
s2 = input()
st = []

for c in s1 + s2:
    if c == '~':
        top = st.pop() # 스택에 A가 있고 현재 A~가 만들어진 경우 상쇄
        if st and st[-1] == top:
            st.pop()
        else:
            st.append(top + '~')
            
    else: # 스택 top이 A~인데 현재 A가 들어온 경우 상쇄
        if st and st[-1] == c + '~':
            st.pop()
        else:
            st.append(c)

if not st:
    print("YES")
else:
    print("NO")