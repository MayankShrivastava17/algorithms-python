def binary_search(arr, low, high, x): # x is the element we're looking for
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
  
size = int(input("Enter the size of array: "))

array = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]
element = int(input("Enter the element to search: "))
  
result = binary_search(array, 0, len(array) - 1, element)
  
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
