def findDay(weights, capacity):
    n = len(weights)
    load = 0
    day = 0
    for i in range(n):
        if load + weights[i] <= capacity:
            load += weights[i]
        else:
            day += 1
            load = weights[i]
    return day + 1  # Include the last day

def leastWeightCapacity(weights, d):
    total_weight = sum(weights)
    low = max(weights)
    high = total_weight

    while low <= high:
        mid = (low + high) // 2
        n_d = findDay(weights, mid)
        if n_d <= d:
            high = mid - 1
        else:
            low = mid + 1
    return low

# Sample Input 1
weights1 = [5, 4, 5, 2, 3, 4, 5, 6]
d1 = 5
result1 = leastWeightCapacity(weights1, d1)
print(result1)  # Output: 9

# Sample Input 2
weights2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d2 = 1
result2 = leastWeightCapacity(weights2, d2)
print(result2)  # Output: 55
