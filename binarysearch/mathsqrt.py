import math
def floorsqrt(m):
    ans=0
    ans=int(math.sqrt((m)))
    return ans
if __name__=="__main__":
    m=int(input("enter the number to find the square root"))
    ans=floorsqrt(m)
    print("squareroot is ",ans)