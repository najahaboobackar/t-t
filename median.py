def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)

    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (nums[mid1] + nums[mid2]) / 2
    else:
        mid = n // 2
        median = nums[mid]

    return median

if __name__ == "__main__":
    arr1 = [2, 4, 6]
    arr2 = [1, 3, 5]
    ans = findMedianSortedArrays(arr1, arr2)
    print("The median is", ans)
