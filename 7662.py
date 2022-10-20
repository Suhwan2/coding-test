import heapq
from sys import stdin as st

t=int(input())

for _ in range(t):
    k=int(input())
    heap=[]
    mheap=[]
    for i in range(k):
        word=st.readline().strip().split()
        a,b=word[0],int(word[1])
        if a=='I':
            heapq.heappush(heap,b)
            heapq.heappush(mheap,(-b,b))
        else:
            if b=='1':
                if mheap:
                    heapq.heappop(mheap)
            else:
                if heap:
                    heapq.heappop(heap)
    if mheap and heap:
        print(mheap[0],heap[0])
    elif mheap:
        print(mheap[0],mheap[0])
    elif heap:
        print(heap[0],heap[0])
    else:
        print('EMPTY')