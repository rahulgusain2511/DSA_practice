def rotateArray(arr,n):
    z=arr[0]
    for i in range(1,n-1):
        arr[i-1],arr[i]=arr[i],arr[i+1]
    arr[n-1]=z
    return arr