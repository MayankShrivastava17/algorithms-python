
 
def interpolationSearch(arr, lo, hi, x):
 
   
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
 
        
        if arr[pos] == x:
            return pos
 
       ]
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
 
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1
 
n = int(input("Enter the size of array : "))

arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]
x=int(input("Enter element to search : "))

index = interpolationSearch(arr, 0, n - 1, x)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")