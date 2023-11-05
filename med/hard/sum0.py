def main():
    arr=[-1,0,1,2,-1,-1]
    n=len(arr)
    sum0(arr,n)
def sum0(arr,n):
    
    s=0
    count=0
    right=0
    left=0
    
    temp=[]
    for i in range(n):
        s+=arr[i]
        right+=1
       
        if s==0:
            while left <right:
                temp.append(arr[left])
                left+=1
    for s in temp:
        print(s,end=" ")            
main()                
            
        
        
            