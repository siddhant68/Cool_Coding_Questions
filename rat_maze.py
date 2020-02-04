def findPath(arr, n):
    sol = [[0] * n for i in range(n)]
            
    printMatrix(arr)
    findPathRec(arr, 0, 0, sol, n)

def findPathRec(arr, x, y, sol, n):
    if x == n-1 and y == n-1:
        sol[x][y] = 1
        printMatrix(sol)
        return
    
    
    if x>=n or x<0 or y>=n or y<0 or sol[x][y]==1 or arr[x][y]==0:    
        return
    
    sol[x][y] = 1
    
    findPathRec(arr, x-1, y, sol, n)
    findPathRec(arr, x+1, y, sol, n)
    findPathRec(arr, x, y-1, sol, n)
    findPathRec(arr, x, y+1, sol, n)
    
    sol[x][y] = 0

def printMatrix(arr):
    for i in arr:
        for j in i:
            print(j, end=' ', sep=' ')
        print()
    print('------------------------------------------')
    
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        print(findPath(matrix, n[0]))
