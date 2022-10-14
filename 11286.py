from sys import stdin as st
import heapq

n=int(st.readline())

heap=[]

for _ in range(n):
    x=int(st.readline())
    if x:
        heapq.heappush(heap,(abs(x),x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print('0')