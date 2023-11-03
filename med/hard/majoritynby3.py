def  main():
    arr=[3,3,3,2,1,4,4,4,4,4]
    n=len(arr)
    majority(arr,n)
def majority(arr,n):
    i=0
    j=1
    count=0
    m=[]
    for i in range(n):
        min=i
        for j in range(n):
            if min==arr[j]:
                count+=1
            if count>=n//3:
                m.append(arr[j])
                
                count=0
            
    m=set(m)            
    for s in m:
        print(s)
      
          
main()              
                    
                
    