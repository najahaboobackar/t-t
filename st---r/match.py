
ch = int(input("enter the value"))
a=[3]
match ch:
    case 1:
        a[0]=float(input("enter the radius"))
        print(3.14*a[0]*a[0])
    case 2:
        a[0]=float(input("enter the length"))
        a[1]=float(input("enter the breadth"))
        print(a[0]*a[1])
    case _:
        print("invalid")    
            
            
       
