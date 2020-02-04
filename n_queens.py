def isSafe(matrix, x, y):
    for i in range(x):
        if matrix[i][y] == 'Q':
            return False
    
    i = x-1
    j = y-1
    
    while i >= 0 and j >= 0:
        if matrix[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    i = x-1
    j = y+1
    
    while i >= 0 and j < n:
        if matrix[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def findPositions(matrix, n, count):
    if count == n:
        for i in matrix:
            for j in i:
                print(j, sep=' ', end=' ')
            print()
        print('\n----------------------\n')
        return
        
    for j in range(n):
        if isSafe(matrix, count, j):
            matrix[count][j] = 'Q'
            
            findPositions(matrix, n, count+1)
            
            matrix[count][j] = '_'
      

# Driver Program
if __name__=='__main__':
    n = int(input())
    matrix = [['_'] * n for i in range(n)]
    findPositions(matrix, n, 0)