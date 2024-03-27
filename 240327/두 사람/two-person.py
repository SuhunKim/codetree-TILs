y1,m1 = map(str,input().split())
y2,m2 = map(str,input().split())

y1,y2 = int(y1),int(y2)

if (y1>=19 and m1=="M") or( y2>=19 and m2=="M"):
    print(1)
else:
    print(0)