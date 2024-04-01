#from collections import deque
from queue import Queue

L,Q = map(int, input().split())     #1<= Q 3<= L <=10000 

q = Queue()

for x in range(Q):
    #ORDER 1: 초밥 , 2: 손님 3: 사진 시각 t(1씩 증가할 때마다 "x는 시계방향으로 회전)""
    #초빕 만들기    100 t x name    (t에 입장, x 위치, name초밥을 하나
    #손닙입장       200 t x name n  (t에 입장, x위치, name 이름, n개) 먹고 자리를 떠남
    # 사진 촬영     300 t           시각 t에  사람 수 남은 초밥 수 출력
    noworder=[]
    noworder.append(input().split())
    order = len(noworder)
    
    if order == 2:   #사진촬영



    elif order == 3: #초밥 만들기


    elif order==4:  #손님 입장