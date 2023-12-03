from math import ceil
import sys


def timelyhours(arr,i):
    n=len(arr)
    th=0
    for k in range(n-1):
        th+=ceil(arr[k]/i)
    return th   

def binarysearch(arr,h):
    low=1
    high=max(arr) 
    while low<=high:
        mid=(low+high)//2
        timet=timelyhours(arr,mid)
        if timet<=h:
            high=mid-1
        else:
            low=mid+1
    return low  
 
if __name__=="__main__":
    arr=[7, 15, 6, 3]
    h=8
    ans=binarysearch(arr,h)
    print("this much hour took to eat all those bananas",ans)         
        