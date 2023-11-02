def main():
    arr=[3,4,7,2,-3,1,4,2,1]
    k=int(input("enter the number"))
    
    subcount(arr,k)
def subcount(arr,k):
    n=len(arr)
    sumdict={0:1}
    count=0
    s=0
    for num in arr:
        s+=num
        if s-k in sumdict:
            count+=sumdict[s-k]
        if s in sumdict:
            sumdict[s]+=1
                
        else :
            sumdict[s]=1
    print(count)    
main()    