import sys

def maxSubArraySum(a,size):
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far
    
n = int(input("Enter the size of array : "))
arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]
print (f'Max Sub Array Sum using Kadane\'s Algorithm is {maxSubArraySum(arr, n)}')
