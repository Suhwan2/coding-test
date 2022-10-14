from sys import stdin as st
import heapq

t=int(st.readline())

for _ in range(t):
    n=int(st.readline())
    heap=list(map(int,st.readline().split()))
    heapq.heapify(heap)
    cnt=0
    while len(heap)>=2:
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        heapq.heappush(heap,a+b)
        cnt+=a+b

    print(cnt)