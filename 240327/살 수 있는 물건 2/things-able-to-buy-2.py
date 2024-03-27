n= int(input())

dict_p = {}
list_p = [["book",3000],["mask",1000],["pen",500]]

list_p = sorted(list_p,key = lambda x:(-x[1]))
answer = "no"
for i in range(len(list_p)):
    if list_p[i][1]<=n:
        answer = list_p[i][0]
        break
        #print(list_p[i][0])

print(answer)