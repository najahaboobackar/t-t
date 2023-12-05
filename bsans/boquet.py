def possible(arr,day,m,k):
    n=len(arr)
    count1=0
    no_of_b=0
    for i in range(n-1):
        if arr[i]>=day:
            count1+=1
        else:
            no_of_b+=(count1)//k  
            count1=0
        no_of_b+=(count1)//k  
        return no_of_b>m   
def bsb()    
              