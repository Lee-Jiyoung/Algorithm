#https://www.acmicpc.net/problem/9655

def cal(n:int) -> int:
    dp = [1,2,3]
    for i in range(3,n):
        dp.append(dp[i-3]+1)
    return dp[n-1]

cn = int(input())
res  = "CY" if  cal(cn)%2 == 0 else "SK"
print(res)