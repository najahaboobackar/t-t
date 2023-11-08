n=int(input("enter the limit"))
list1=[]
for i in range(n):#thiis for column
    temp_list=[] #temp_list is added at each row
    for j in range(i+1):
        if j==0 or j==i:
            temp_list.append(1)# add 1 to end  and start
        else:
            temp_list.append(list1[i-1][j]+list1[i-1][j-1])  #previous number addition
    list1.append(temp_list)       
print(list1)   

for i in range(n):
    for j in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print(list1[i][j],end=" ")
    print()             