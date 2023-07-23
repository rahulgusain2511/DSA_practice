def largestElement(arr: [], n: int):
    max=arr[0]
    for i in range (n):
        if arr[i]>max:
            max=arr[i]
    return max
