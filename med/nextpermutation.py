class Solution:
    @staticmethod
    def permutations(arr):
        length = len(arr)
        if length <= 2:
            return arr.reverse()
        
        pointer = length - 2
        while pointer >= 0 and arr[pointer] >= arr[pointer + 1]:
            pointer -= 1
            
        if pointer == -1:
            arr.reverse()
            return arr
        
        for x in range(length - 1, pointer, -1):
            if arr[pointer] < arr[x]:
                arr[pointer], arr[x] = arr[x], arr[pointer]
                break
        
        arr[pointer+1:] = reversed(arr[pointer+1:])
        return arr

# Test the code
arr = [1, 2, 3]
obj = Solution()
print(obj.permutations(arr))  # This should print the next permutation
