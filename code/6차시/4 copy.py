n, m, k= map(int, input().split())

def b(start, selected, current_sum):
    if current_sum > k:
        return 0
    
    if selected == m:
        if current_sum == k:
            return 1

    count = 0
    for i in range(start, n+1):
        count += b(i+1, selected+1, current_sum+i)
    return count

print(b(1, 0 ,0))

        