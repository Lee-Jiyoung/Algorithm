# https://www.acmicpc.net/problem/2309

l = []
res=0
for i in range(9):
    n = int(input())
    l.append(n)
    res +=n
l = sorted(l)

x,y=0,0
check = False
for i in range(8):
    for j in range(i+1,9):
        if res-l[i]-l[j]==100:
            x = i
            y = j
            break

for i in range(9):
    if i == x or i== y:
        continue
    print(l[i])