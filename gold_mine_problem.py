import numpy as np

def soln(matrix, summ):
    for j in range(1, n):
        for i in range(m):
            if i == 0:
                matrix[i][j] += max(matrix[i][j-1], matrix[i+1][j-1])
            elif i == m-1:
                matrix[i][j] += max(matrix[i][j-1], matrix[i-1][j-1])
            else:
                matrix[i][j] += max(matrix[i][j-1], matrix[i-1][j-1], matrix[i+1][j-1])
              
for _ in range(int(input())):
    m, n = map(int, input().split())
    l = [int(x) for x in input().split()]
    matrix = np.array(l)
    matrix = matrix.reshape(m, n)
    matrix = matrix.tolist()
    
    soln(matrix, max(matrix, key=lambda x: x[0])[0])

print(matrix)
print(max(matrix, key=lambda x: x[n-1])[n-1])