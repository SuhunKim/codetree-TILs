a = int(input())

ans=[]

for i in range(a+1):
    if i%2==0 and i%4!=0 :
        continue
    elif (i//8)%2==0:
        continue
    elif i%7<4:
        continue
    else:
        ans.append(str(i))

print(' '.join(ans))