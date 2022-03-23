def countingSort(arr):
    upper = max(arr)
    r = [0] * (upper + 1)
    for j in range(upper + 1):
        if j in arr:
            r[j] += (arr.count(j))

    return(r)

print(countingSort([1,1,3,2,1]))