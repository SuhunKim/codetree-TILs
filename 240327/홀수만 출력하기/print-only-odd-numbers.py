n = int(input())

list_n=[]

for i in range(n):
    list_n.append(int(input()))

#list_n.sort()

for i in range(len(list_n)):
    if list_n[i]%3==0 and list_n[i]%2==1 and list_n[i]!=0:
        print(list_n[i])