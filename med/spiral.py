n=int(input("enter the  rows"))
m=int(input("enter teh column"))
a=[]
for i in range(m):
    b=[]
    for j in range(n):
        val=int(input(f"enter the number {i} {j}"))
        b.append(val)
    a.append(b)
print(a)  

row=0
col=0
while row<m and col<n: #when row is less than m
    #col when n is less
    for i in range(col,n):
        print(a[row][i],end=" ")# when row is constant print the first row
    row+=1
    for i in range(row,m):#print the last column
        print(a[i][n-1],end= " ") 
    n=n-1
    if row<m:
        for i in range(n-1,col-1,-1) : #print the last row
            print(a[m-1][i],end=" ")  
        m-=1  
        for i in range(m-1,row-1,-1):#print  the first column
            print(a[i][col] ,end=" ") 
            col+=1           