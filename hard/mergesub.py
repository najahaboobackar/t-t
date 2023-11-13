arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
n=len(arr)
ans=[]
arr.sort()
for i in range(n):
    if not ans or arr[i][0] > ans[-1][1]:
        ans.append(arr[i])
    else:
        ans[-1][1] = max(ans[-1][1], arr[i][1]) 
print(ans)            