arr=[1,2,3,1,5]
n1=len(arr)
s=0
s2=0
sn=(n1*(n1+1))//2
s2n=(n1*(n1+1)*(2*n1+1))//6
for i in range(n1):
    s+=arr[i]
    s2+=arr[i]*arr[i]
val1=s-sn
val2=s2-s2n
val2=val2//val1
x=(val1+val2)//2
y=x-val1
print(x,y)   