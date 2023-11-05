def main():
    arr=[5,5,5,5,5,6,6,6,6,6]
    n=len(arr)
    majorityby3(arr,n)
    
def majorityby3(arr,n):
    x=-1
    y=-1
    k=[]
    countx=0
    county=0
    count=n//3
    for i in range(n):
        if x==arr[i]:
            countx+=1
            if countx>count:
                num=arr[i]
                k.append(num)
            
        elif y==arr[i]:
            county+=1
            if county>count :
                num1=arr[i]
                k.append(num1)
           
        elif countx==0:
            x=arr[i]
            countx=1
        elif county==0:
            y=arr[i]
            county=1 
        else:
            countx-=1
            county-=1

    k=list(set(k))      
    print(k)               
main()            
    
            
                          
               