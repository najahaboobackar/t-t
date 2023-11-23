def main():
    arr=[1,2,2,3]
    n=len(arr)
    x=3
    y=lowerBound(arr,n,x)
    print(y)
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    arr.sort()
    for i in range(n-1):
        if arr[i]>=x:
            return i
    return n        
main()