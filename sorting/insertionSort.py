def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

n = int(input("Enter the size of array : "))

arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]

print("Array entered")
print(arr)

arr = insertionSort(arr)

print("Array after sorting the elements")
print(arr)
