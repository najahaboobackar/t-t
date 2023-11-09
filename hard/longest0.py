arr=[9, -3, 3, -1, 6, -5]
n=len(arr)
maxi=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum==0:
            maxi=max(maxi,j-i+1)
print(maxi)            
            