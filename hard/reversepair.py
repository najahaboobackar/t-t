def main():
    arr=[1,3,2,3,1]
    n=len(arr)
    r=team(arr,n)
    print(r)
def team(arr,n):
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>2*arr[j]:
                count+=1
    return count
main()            
        