def bubble_sort(arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]





if __name__ == '__main__':
    arr = [77,12,3,4,55,66,123,1,90]
    n = len(arr)
    bubble_sort(arr, n)
    print(arr)