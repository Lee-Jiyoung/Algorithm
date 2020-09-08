#https://www.acmicpc.net/problem/9461

n = int(input())
t = []
P = [0,1,1,1]
for i in range(n):
    tmp = int(input())
    t.append(tmp)

for i in t:
    if i<len(P)-1:
        continue
    for j in range(len(P),i+1):
        P.append(P[j-2]+P[j-3])

for i in t:
    print(P[i])