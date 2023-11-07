def main():
    arr=[1,0,-2,-1,3,-3,4,8,-4]
    n=len(arr)
    quad(arr,n)
def quad(arr,n):
    ans=[]
    for i in range(0,n-4):
        for j in range(i+1,n-3):
            for k in range(j+1,n-2):
                for l in range(k+1,n-1):
                    sum=arr[i]+arr[j]+arr[k]+arr[l]
                    if sum==0:
                        temp=[arr[i],arr[j],arr[k],arr[l]] 
                        ans.append(temp)  
        
    print(ans) 
main()                    
                