#https://www.acmicpc.net/problem/2688

def sum(l:list,n) -> int:
    s = 0
    for i in range(n):
        s += l[i]
    return s

def cal(n:int) -> int:
    d = [[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]]
    for i in range(1,n):
        t = list([sum(d[i],j+1) for j in 10])
        for j in range(10):
           t.append(sum(d[i],j+1))
        d.append(t)
    return sum(d[n],10)

cn = int(input())
res = []

for i in range(cn):
    t = int(input())
    res.append(cal(t))

print("\n".join(str(i) for i in res))