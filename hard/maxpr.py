arr=[1,2,3,-4,-5]
n=len(arr)
product1=0
product=0
for i in range(n-1):
    for j in range(i+1,n):
        product=arr[i]*arr[j]
        product1=max(product1,product)
print(product1)        
        
        