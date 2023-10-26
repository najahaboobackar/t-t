def main():
    arr=[1,2,3,4,5,9,8]
    ans=longest(arr)
    print(ans)
def longest(arr):
    cnt=0
    long=0
    st=set(arr) 
    for it in st:
        if it-1 not in st:
            cnt=1
            x=it 
            while x+1 in st:
                x+=1
                cnt+=1
                long=max(long,cnt) 
    return long     
main()       
