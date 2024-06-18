a=input().lower()
res=[]
for i in a:
    if i in a.lower():
        res.append(i)
        res.sort()
print("".join(res))

