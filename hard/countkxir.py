from collections import defaultdict
arr=[4, 2, 2, 6, 4]
n=len(arr)
xr=0
k=6
mpp=defaultdict(int)
mpp[xr]=1
count=0
for i in  range(n):
    xr^=arr[i]
    x=xr^k
    count+=mpp[x]
    mpp[xr]+=1
print(count)    
    