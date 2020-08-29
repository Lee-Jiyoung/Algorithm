#https://www.acmicpc.net/problem/9012

def cal(l:list)->str:
    t=[]
    res="YES"
    for i in l:
        if i =="(":
            t.append(i)
        else:
            try:
                if t.pop()=="(":
                    pass
            except:
                res = "NO"
                break
    if t:
        res = "NO"
    return res

result = []
a = int(input())
for i in range(a):
    t = input()
    result.append(cal(list(t)))

for i in result:
    print(i)
