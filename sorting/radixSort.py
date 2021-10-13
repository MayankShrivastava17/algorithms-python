# this is a py program for radix sort

def countingSort(arr, exp1):
	n = len(arr)
	output = [0] * (n)
	count = [0] * (10)
	for i in range(0, n):
		index = (arr[i]/exp1)
		count[int((index)%10)] += 1
	for i in range(1,10):
		count[i] += count[i-1]
	i = n-1
	while i>=0:
		index = (arr[i]/exp1)
		output[ count[ int((index)%10) ] - 1] = arr[i]
		count[int((index)%10)] -= 1
		i -= 1
	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

def radixSort(arr):
	max1 = max(arr)
	exp = 1
	while max1/exp > 0:
		countingSort(arr,exp)
		exp *= 10

n = int(input("Enter the size of array : "))
arr = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]

print ("Array Before Sorting:: ")
print (arr)

radixSort(arr)
print ("Array After Using Radix Sort :: ")
print (arr)
