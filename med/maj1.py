def main():
    arr=[2,2,2,2,2,2,1,1,1]
    n=len(arr)
    majority(arr,n)
    
def majority(arr,n):
    cnt=0
    el=None
    for i in range(n-1):
        if cnt==0:
            cnt=1
            el=arr[i]
        elif el==arr[i]:
            cnt+=1
        else:
            cnt-=1  
    cnt2=0 
    for i in range(n-1): 
        if el==arr[i]:
            cnt2+=1
    if cnt2>n/2:
        print(el)                 
main()                     