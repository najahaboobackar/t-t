arr=[1, 2, -3, 0, -4, -5]
pre=0
suff=0
ans=0
n=len(arr)
for i in range(n-1):
    if pre==0:
        pre=1
    if suff==0:
        suff=1
    pre*=arr[i]
    suff*=arr[n-i-1]
    ans=max(ans,max(pre,suff))   
print(ans)         
    