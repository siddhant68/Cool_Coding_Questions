def count_path(matrix, x, y, m, n):
    if x == m-1 and y == n-1:
        return 1
    
    if x > m-1:
        return 0
    
    if y > n-1:
        return 0
    
    return count_path(matrix, x+1, y, m, n) + count_path(matrix, x, y+1, m, n)

for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    matrix = [[0] * m for _ in range(n)]
    print(count_path(matrix, 0, 0, m, n))
