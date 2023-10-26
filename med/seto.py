matrix = [
    [1, 0, 1],
    [1, 1, 1],
    [1, 2, 2]
]
m,n=len(matrix),len(matrix[0])
row,col=[1]*m,[1]*n
for r in range(m):
    for c in range(n):
        if matrix[r][c]==0:
            row[r]=0
            col[c]=0
for r in range(m):
    if row[r]==0:
        matrix[r]=[0]*m  
for c in range(n):
    if col[c]==0:
        for i in range(m):
            matrix[i][c]=0
print(matrix)                             