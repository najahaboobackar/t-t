arr=[1,2,3,1,0,-1,-2,-1,-3,9,1,1,1,1]
n=len(arr)
hash={0:1}
maxi=0
sum=0
for i in range(n):
    sum+=arr[i]
    if sum==0:
        maxi=i+1
    if sum in hash:
        maxi=max(maxi,i-hash[sum]) 
    else:
        hash[sum]=i
print(maxi)        
      