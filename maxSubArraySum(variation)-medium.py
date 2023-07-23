def maxSubArraySum(self,arr,N):
# Initialize variables

    max_sum = arr[0]
    current_sum = arr[0]

    # Traverse the array
    for i in range(1, N):
        # Calculate the current sum including the current element
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update the maximum sum if necessary
        max_sum = max(max_sum, current_sum)

    return max_sum