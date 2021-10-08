def countingSort(arr):
    n = len(arr)
    max_of_arr = max(arr)
    count = [0 for i in range(max_of_arr+1)]
    for i in arr:
        count[i] += 1
    ind = 0
    for i in range(max_of_arr+1):
        c = count[i]
        while c:
            arr[ind] = i
            ind += 1
            c -= 1
    return arr

n = int(input("Enter the size of array : "))

arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]

print("Array entered")
print(arr)

countingSort(arr)

print("Array after sorting the elements")
print(arr)
