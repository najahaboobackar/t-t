def main():
    arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target=int(input("enter "))
    n = len(arr)
    sumfour(arr, target, n)

def sumfour(arr, target, n):
    
    ans = []
    arr.sort()
    for i in range(n-1):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n-1):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = n-1
            while k < l:
                _sum = arr[i] + arr[j] + arr[k] + arr[l]
                if _sum == target:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    ans.append(temp)
                    k+=1
                    l-=1
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l-1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1
    print(ans)

main()
