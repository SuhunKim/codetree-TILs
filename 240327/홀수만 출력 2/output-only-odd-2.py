b,a = map(int,input().split())

for i in range(b+1,a-1,-1):
    if i%2==1:
        print(i,end=' ')