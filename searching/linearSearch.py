def search(arr, n, x):
	for i in range(0, n):
		if (arr[i] == x):
			return i
	return -1

n = int(input("Enter the size of array : "))
arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]
x=int(input("Enter the element to search : "))

result = search(arr, n, x)

if(result == -1):
	print("Element is not present in array")
else:
	print("Element is present at index", result)
