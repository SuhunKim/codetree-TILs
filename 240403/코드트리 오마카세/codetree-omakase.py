# from queue import Queue

# l,q = map(int,input().split())

# list_order = []
# que = Queue()

# for i in range(q):
#      list_order.append(int(input()))

#모범 답안
L,Q = 0,0

class Query :
     def __init__(self, cmd, t, x, name, n):
          self.cmd = cmd
          self.t = t
          self.x = x
          self.name = name
          self.n = n

queries= [] # 명령을 추가 

names = set() # 등장 사람 목록, 중복제외용 set (list는 중복허용)

p_queries = {} # 사람마다 주어진 초밥 명령 (cmd) 관리 

entry_time = {} # 사람마다 입장시간 관리

position = { } #사람마다 위치 관리

exit_time = {} # 사람마다 퇴장시간 관리

def cmp(q1,q2):     # Query를 t,cmd 순으로 정렬
     if q1.t != q2.t:
          return q1.t<q2.t
     return q1.cmd<q2.cmd

#Input
L,Q = map(int, input().split())
for _ in range(Q):
     command = input().split()
     cmd,t,x,n = -1,-1,-1,-1
     name=""
     cmd = int(command[0])
     if cmd==100:
          t,x,name = command[1:]
          t,x = map(int, [t,x])
     elif cmd==200:
          t,x,name,n=command[1:]
          t,x,n = map(int,[t,x,n])
     else: #cmd==300
          t = int(command[1])

     queries.append(Query(cmd, t,x,name,n)) # 쿼리 명령문 등록


     if cmd ==100: #사람별 주어진 초밥 목록 관리
          if name not in p_queries:
               p_queries[name]=[]
          p_queries[name].append(Query(cmd, t, x, name, n))

     elif cmd ==200: # 손님 입장시간, 위치
          names.add(name) #set()
          entry_time[name] = t
          position[name] = x

# 사람 별 이름과 맞는 조합을 언제 먹는지 계산한 정보를 기존 query에 추가(111번 쿼리)
for name in names:
     #name 별 퇴장 시간 관리 = 마지막으로 먹는 초밥 중 가장 늦은 시간
     exit_time[name]=0

     for q in p_queries[name]: 
          time_to_removed = 0      
          if q.t < entry_time[name]:    #초밥이 사람 등장 전에 주어진 경우
               t_sushi_x = (q.x+ (entry_time[name]-q.t)) %L # entrytime 시 스시위치
               additional_time = (position[name] - t_sushi_x+L) % L

               time_to_removed = entry_time[name] + additional_time
     
          else:               # 초밥이 사람 등장 이후 주어진 경우
               additional_time = (position[name] - q.x +L)%L
               time_to_removed = q.t+additional_time   # 초밥-사람 몇초가 지나야 만나는지 계산 
          
          exit_time[name] = max(exit_time[name], time_to_removed) # 가장늦게 초밥이 사라지는 시간

          queries.append(Query(111,time_to_removed,-1,name,-1)) # 초밥이 사라지는 111번 쿼리를 추가

# 사람마다 초밥을 마지막으로 먹은 시간 t를 계산, 그 사람이 해당 t 때 떠났다는 Query 222번을 추가
for name in names:
     queries.append(Query(222,exit_time[name], -1,name,-1))


# 전체 쿼리를 시간 순 정렬, t가 일치 시 사진 촬영이  가장늦도록 cmd (100, 200, 300) 순으로 정렬
queries.sort(key = lambda q: (q.t,q.cmd))

# 이후 순서대로 사람, 초밥 수 count -> 300이 나오면 현재 사람, 초밥 수 출력
people_num  , sushi_num = 0,0
for i in range (len(queries)):
     if queries[i].cmd ==100:
          sushi_num+=1
     elif queries[i].cmd ==111:
          sushi_num-=1
          
     elif queries[i].cmd ==200:
          people_num+=1

     elif queries[i].cmd ==222:
          people_num-=1
          

     else: # 사진 촬영 시, 답 을 출력 
          print(people_num,sushi_num)