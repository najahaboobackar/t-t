def main():
    arr=[1,2,3,-1,-2,-3]
    n=len(arr)
    alternative(arr,n)
def alternative(arr,n):
    pos=[]
    neg=[]
    
    for i in range(n-1):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(len(pos)):
        arr[2*i] =pos[i]
    for i in range(len(neg)):    
        arr[2*i+1]=neg[i]
    
    print(arr) 
main()                       