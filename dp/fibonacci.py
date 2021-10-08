'''
Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, ....
Fib(0) = 0
Fib(1) = 1
Fib(N) = Fib(N-1) + Fib(N-2)    for N>1

This program uses dynamic programming to solve this
Time complexity : O(N)
'''

n = int(input("Howmany terms of series do you want to print? "))

dp = [0,1]

for i in range(n-1):
    dp.append( dp[i] + dp[i+1] )

print("The first n terms of Fibonacci series are: ")
print(*dp)
