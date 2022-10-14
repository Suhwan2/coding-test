from sys import stdin as st
import heapq

n=int(st.readline())

max_h=[]
min_h=[]

for _ in range(n):
    x=int(st.readline())
    if len(max_h)==len(min_h):
        heapq.heappush(max_h,(-x,x))
    else:
        heapq.heappush(min_h,(x,x))
    if max_h and min_h:
        while True:
            m=max_h[0][1]  
            M=min_h[0][1]
            if m>M:
                heapq.heappop(max_h)
                heapq.heappop(min_h)
                heapq.heappush(max_h,(-M,M))
                heapq.heappush(min_h,(m,m))
            else:
                break
    print(max_h[0][1])
