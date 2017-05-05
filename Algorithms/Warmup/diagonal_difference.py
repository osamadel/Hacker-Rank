def absDiff(mat):
        
    n = len(mat)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += mat[i][i]
    for i in range(n):
        sum2 += mat[i][n-i-1]    
    return abs(sum1 - sum2)
    
mat = []
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

print(absDiff(mat))