def main():
    arr=[1,1,2,2,3,3,4,5,4]
    r=unique(arr)
    print(r)
def unique(arr):
    ans=0
    for num in arr:
        ans=ans^num
    return ans      
main()      
            
            
        
            
               
                    
                
                    