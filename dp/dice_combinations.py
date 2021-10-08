'''
Dice Combinations

Task is to count the number of ways to construct sum n
by throwing a dice one or more times. Each throw produces
an outcome between 1 and 6.

For example, if n=3, there are 4 ways:
* 1+1+1
* 1+2
* 2+1
* 3

'''

n = int(input("Enter the value of n: "))

dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n+1):
    dp[i] += dp[i-1]
    if i>1:
        dp[i]+=dp[i-2]
    if i>2:
        dp[i]+=dp[i-3]
    if i>3:
        dp[i]+=dp[i-4]
    if i>4:
        dp[i]+=dp[i-5]
    if i>4:
        dp[i]+=dp[i-6]

print(dp[n])
