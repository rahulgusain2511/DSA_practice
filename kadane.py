import sys

def maxSubArraySum(self,arr,N):
    maxi = -sys.maxsize-1 # maximum sum
    sum = 0
    for i in range(N):
        sum += arr[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
    return maxi
        
"""

follow up 
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    sum = 0

    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")


    .......
def maxSubarraySum(arr, n) :
    maxi = -sys.maxsize-1 # maximum sum
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
        if maxi < 0:
            maxi=0
    return maxi
"""