#https://www.acmicpc.net/problem/13301

def cal(n:int) -> int:
    dp=[1,2]
    if n==1:
        res = dp[1]*2
    else:
        for i in range(2,n+1):
            dp.append(dp[i-2]+dp[i-1])
        res = dp[n]*2
    return res

n = int(input())
print(cal(n))