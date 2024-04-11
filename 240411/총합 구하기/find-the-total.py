a,b= map(int, input().split())
ans = []
for i in range(a,b+1,1):
    if i%6==0 and i%8!=0:
        ans.append(i)

print (sum(ans))