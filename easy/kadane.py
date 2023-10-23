def main():
    arr=[4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
    n=len(arr)
    kadane(arr,n)
def kadane(arr,n):
    curr_sum=0
    st=0 
    en=0
    poi=0
    max=0
    for i in range(0,n-1):
        curr_sum=curr_sum+arr[i]
        if max <curr_sum:
            st=poi
            en=i
            max=curr_sum
        if curr_sum<0:
            poi=i+1
            curr_sum=0
    print(max) 
    for j in range(st, en+1):
        b=arr[j]
        print(b)
main()             