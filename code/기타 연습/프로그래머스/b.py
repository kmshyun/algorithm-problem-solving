def solution(s):
    st = []
    st.append(s[0])
    for i in range(1, len(s)):
        if st == []:
            st.append(s[i])
        elif st [-1] != s[i]:
            st.append(s[i])
        else:
            st.pop()

    return int(bool(st)) + 1

'''
순서대로 읽으면서 pop
abba
[a]
[a, b]
[a]
[]

'''