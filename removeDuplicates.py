def removeDuplicates(arr,n):
    i=0
    for j in range(1,n):
        if arr[j]!=arr[i]:
            arr[i+1],arr[j]=arr[j],arr[i+1]
            i+=1
    return i+1