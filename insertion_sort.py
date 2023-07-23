def insertion_sort(arr, n):
    for i in range(1,n):
        c=i
        while c>0 and arr[c]<arr[c-1]:
            arr[c], arr[c-1] = arr[c-1], arr[c]
            c-=1






if __name__ == '__main__':
    arr = [77,12,3,4,55,66,123,1,90]
    n = len(arr)
    insertion_sort(arr, n)
    print(arr)