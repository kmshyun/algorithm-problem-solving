a, b, s, t = map(int, input().split())
g = {i:[] for i in range(1, a+1)}

for _ in range(b):
    k, l = map(int, input().split())
    g[k].append(l)
    g[l].append(k)

# 이건 걍 외운다 생각하자!
v = [0] * (a + 1) # <-- 노드가 문자열이면 set을 사용해야함!
# visited.add(v)

def dfs(s):
    v[s] = True
    for i in g[s]:
        if not v[i]:
            dfs(i)

c = 0
dfs(s)
print("YES" if v[t] else "NO")

# DFS는 LIFO 방식으로서, stack과 같은 원리로 구현됨!
# 스택을 만들어서 구현하는 DFS 방법도 존재


# graph = {i:[] for i in range(1, a+1)}
# graph를 dictionary 로 만드는 방법