from sys import stdin as st
import heapq

n=int(st.readline())

heap=[]

for _ in range(n):
    x=int(st.readline())
    if x:
        heapq.heappush(heap,x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print('0')