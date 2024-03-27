a,b = map(int, input().split())

list_a = []

#for i in range(b+1,a-1,-1):
for i in range(a,b+1,1):
    if i%2==1:
        print(i,end = ' ')

    #     list_a.append()