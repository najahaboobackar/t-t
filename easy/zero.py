def main():
    arr = [1, 0, 2, 0, 5, 0, 4]
    n = len(arr)
    zero(arr, n)

def zero(arr, n):
    l = 0
    for r in range(n):
        if arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1

    print(arr)

main()
