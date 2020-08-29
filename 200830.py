#https://www.acmicpc.net/problem/2839

n = int(input())
dp = [-1,-1,1,-1,1]
if n < 6:
    print(dp[n-1])
else:
    for i in range(5,n):
        if dp[i-5] > -1 :
            dp.append(dp[i-5]+1)
            continue
        elif dp[i-3]>-1:
            dp.append(dp[i-3]+1)
            continue
        else:
            dp.append(-1)
    print(dp[n-1])
