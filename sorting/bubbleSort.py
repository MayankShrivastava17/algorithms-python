def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Enter the size of array : "))

arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]

print("Array entered")
print(arr)

bubbleSort(arr)

print("Array after sorting the elements")
print(arr)
