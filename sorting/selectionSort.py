
import sys

n = int(input("Enter the size of array : "))

A = list(map(int, input("Enter the array elements :\n").strip().split()))[:n]


for i in range(len(A)):
	

	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	
	A[i], A[min_idx] = A[min_idx], A[i]


print ("Sorted array")
print(A)
