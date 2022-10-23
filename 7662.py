import heapq
from sys import stdin as st

t=int(input())

for _ in range(t):
    k=int(input())
    heap=[]
    mheap=[]
    visited=[False]*k
    for i in range(k):
        word=st.readline().strip().split()
        a,b=word[0],int(word[1])
        if a=='I':
            heapq.heappush(heap,(b,i))
            heapq.heappush(mheap,(-b,i))
            visited[i]=True
        else:
            if b==1:
                while mheap and not visited[mheap[0][1]]:
                    heapq.heappop(mheap)
                if mheap:
                    visited[mheap[0][1]]=False
                    heapq.heappop(mheap)
            else:
                while heap and not visited[heap[0][1]]:
                    heapq.heappop(heap)
                if heap:
                    visited[heap[0][1]]=False
                    heapq.heappop(heap)
    while mheap and not visited[mheap[0][1]]:
        heapq.heappop(mheap)
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)
    if heap and mheap:
        print(-mheap[0][0],heap[0][0])
    else:
        print('EMPTY')