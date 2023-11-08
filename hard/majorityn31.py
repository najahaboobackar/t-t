def main():
    arr=[1,2,1,1,4,4,2,2,2]
    n=len(arr)
    majorityby3(arr,n)
    
def majorityby3(arr,n):
    x=-1
    y=-1
    k=[]
    countx, county = 0, 0
    
    for i in range(n):
        if x==arr[i]:
            countx+=1
        elif y==arr[i]:
            county+=1
        elif countx==0 and x!=arr[i]:
            x=arr[i]
            countx=1
        elif county==0 and y!=arr[i]:
            y=arr[i]
            county=1 
        else:
            countx-=1
            county-=1
    
    for i in range(n):
        if arr[i] == x:
            countx += 1
        if arr[i] ==y:
            county += 1

    mini = int(n / 3) + 1
    if countx >= mini:
        k.append(x)
    if county >= mini:
        k.append(y)        

    k=list(set(k))      
    print(k)               
main()            
    
            
                          
               