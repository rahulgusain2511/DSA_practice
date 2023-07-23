def selection_sort(arr, n):
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
            arr[mini], arr[i] = arr[i], arr[mini]






if __name__ == '__main__':
    arr = [33,1,2,22,45,121,4,54,67,12]
    n = len(arr)
    selection_sort(arr, n)
    print(arr)