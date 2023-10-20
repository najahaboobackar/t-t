arr=[2,0,1,1]
n=len(arr)
count0=0
count1=0
count2=0
for num in arr:
    if num==0:
        count0+=1
    elif num==1:
        count1+=1
    else:
        count2+=1        

for i  in range(count0):
    arr[i]=0    
for i  in range(count0,count0+count1):
    arr[i]=1
for i  in range(count1+count0,n):
    arr[i]=2
print(arr)                   