#https://www.acmicpc.net/problem/2193

n = int(input())
dp=[0,1,1]
for i in range(3,n+1):
    tmp = dp[i-2]+dp[i-1]
    dp.append(tmp)

print(dp[n])