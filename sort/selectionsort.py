a=[2,4,1,5,7,6,9]
n=len(a)
for i in range(n):
    min=i
    for j in range(i+1,n,1):
        if a[min]>a[j]:
            min=j
        if min!=i:
            a[min],a[i]=a[i],a[min]
for i  in range(0,n):
    b=a[i]
    print(b, end=" ")                