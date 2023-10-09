a=[6,3,5,6,7,42,31,2,1,3,1]
n=len(a)

for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

for i in range(n):
    b=a[i]
    print(b ,end=" ")            