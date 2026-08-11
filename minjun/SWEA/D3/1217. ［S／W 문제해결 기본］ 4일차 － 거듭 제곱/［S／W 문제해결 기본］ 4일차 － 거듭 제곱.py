def multiply(total, n, m):
    m -= 1
    total = total*n
    if m == 0:
        return total
    return multiply(total, n, m)

for i in range(1, 11):
    test_case = int(input())
    n, m = map(int, input().split())  
    print(f"#{test_case} {multiply(n, n, m-1)}")
    
