arr=[1,0,-1,6,9,0]
n=len(arr)
maxi=0
for i in range(n):
    sum=0
    for j in range(n):
        sum+=arr[j]
        if sum==0:
            maxi=max(maxi,j-i+1)
print(maxi)            
            