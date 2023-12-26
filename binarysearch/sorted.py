list1 = [2,4,5]
list2 = [1,3]

# Concatenate and sort the lists
result = sorted(list1 + list2)
low=0
median=0
n=len(result)
high=n-1
mid=int((low+high)//2)
if n%2==0:
    median =float((result[mid]+result[mid+1])/2)
else:
    median =result[mid]    
print(median, result)    
