def canweplacecow(stalls,dis,cow):
    n=len(stalls)
    last=stalls[0]
    cntcow=1
    for i in range(1,n):
        if stalls[i]-last>=dis:
            cntcow+=1
            last=stalls[i]
        if cntcow>=cow:
            return True
    return False
def aggressivecow(stalls,cow):
    n=len(stalls)
    stalls.sort()
    low=0
    high=stalls[n-1]-stalls[0] 
    while high>=low:
        mid=(low+high)//2
        if canweplacecow(stalls ,mid,cow):
            ans=mid 
            low=mid+1
        else:
            high=mid-1
    return high   
if __name__=="__main__":
    stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressivecow(stalls, k)
print("The maximum possible minimum distance is:", ans)               
    