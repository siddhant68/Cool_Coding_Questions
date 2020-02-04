count = 0
def n_queens(n, matrix, row):
    global count
    if row == n:
        print(matrix)
        count += 1
        return
    
    for i in range(n):
        if is_safe(row, i, matrix):
            matrix[row][i] = 1
            n_queens(n, matrix, row+1)
        matrix[row][i] = 0

def is_safe(row, col, matrix):
    i = row-1
    j = col
    while i >= 0:
        if matrix[i][j] == 1:
            return False
        i -= 1
        
    i = row-1
    j = col-1
    while j >= 0 and i >= 0:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    i = row-1
    j = col+1
    while j < len(matrix) and i >= 0:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

n = int(input())
matrix = [[0] * n for i in range(n)]
n_queens(n, matrix, 0)
print(count)
