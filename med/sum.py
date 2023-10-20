def main():
    arr=[1,3,4,6,9,2]
    n=len(arr)
    y=int(input("enter the number"))
    ans=twosum(arr,n,y)
    if ans:
        print("yes sum exists")
def twosum(arr,n,y):
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] +arr[j]==y:
                return True
    return False


main()           