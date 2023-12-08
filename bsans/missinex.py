def kmiss(arr, v):
    n = len(arr)
    j = 1
    i = 0
    while i < n and j <= v:
        if j != arr[i]:
            j += 1
        else:
            i += 1
    return j
#wrong answer
def kthelement(arr, k):
    low = 1
    n = len(arr)
    high = n + k  # Adjust high to include the possible missing elements
    while low <= high:
        mid = (low + high) // 2
        kth = kmiss(arr, mid)
        if kth > k:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    arr1 = [4, 7, 9, 10]
    k1 = 1
    ans1 = kthelement(arr1, k1)
    print(f"For k={k1}, the missing value is {ans1}")

    arr2 = [4, 7, 9, 10]
    k2 = 4
    ans2 = kthelement(arr2, k2)
    print(f"For k={k2}, the missing value is {ans2+1}")
